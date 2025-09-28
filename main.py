# @Author: 4n33sh (Aneesh SP) (aneesh.sp222@gmail.com) 

#! /root/my_virt_envs/bin/python3

#above microprocessor executes code directly form python .venv package. modify to suit your venv. path
#for linux terminal implementation/execution: source /location/to/venv/bin/activate

#before running the script, install dependencies from requirements.txt: pip install -r requirements.txt

import os
import spacy
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from argofloats import floats, profiles
from pyowc import calibration
from utils import helper

from processing import reuse_MITprof as mitprof
from processing import reuse_MITprofAnalysis as mitprof_analysis
from processing import reuse_MITprofStat as mitprof_stat

OWC_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "owc_config.json")
VECTOR_DB_PATH = os.path.join(os.path.dirname(__file__), "vector_db/")

llm = OpenAI(temperature=0)
embeddings = OpenAIEmbeddings()
vectorstore = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embeddings)
nlp = spacy.load("en_core_web_sm")

prompt = PromptTemplate(
    input_variables=["user_query"],
    template="""
    You are FloatChat, an AI assistant for ARGO ocean data.
    Translate the user query into database commands or instructions
    to fetch relevant ARGO profiles (NetCDF/SQL/Vector DB).
    
    Query: {user_query}
    """
)

llm_chain = LLMChain(llm=llm, prompt=prompt)


def retrieve_profiles(float_ids):
    profiles_data = []
    for fid in float_ids:
        p = profiles.getProfiles(fid)
        profiles_data.append(p)
    return profiles_data


def process_profiles(raw_profiles):
    mitprof_data = [mitprof.convert_profile(p) for p in raw_profiles]
    analysis_results = [mitprof_analysis.analyze(p) for p in mitprof_data]
    stats_results = [mitprof_stat.compute_stats(p) for p in mitprof_data]
    return mitprof_data, analysis_results, stats_results


def calibrate_profiles(mitprof_profiles):
    calibrated_profiles = []
    for p in mitprof_profiles:
        calibrated = calibration.run(p, config_path=OWC_CONFIG_PATH)
        calibrated_profiles.append(calibrated)
    return calibrated_profiles


def ingest_to_vector_db(profiles_data):
    docs = [str(p) for p in profiles_data]
    vectorstore.add_texts(docs)
    vectorstore.persist()


def chat_query(user_query):
    doc = nlp(user_query)
    retrieved = vectorstore.similarity_search(user_query, k=3)
    db_results = [r.page_content for r in retrieved]
    llm_input = f"User Query: {user_query}\nRetrieved Profiles: {db_results}"
    response = llm_chain.run(user_query=llm_input)
    return response


def main():
    float_ids = ["5904461", "5904462"]
    raw_profiles = retrieve_profiles(float_ids)
    mitprof_data, analysis_results, stats_results = process_profiles(raw_profiles)
    calibrated_profiles = calibrate_profiles(mitprof_data)
    ingest_to_vector_db(calibrated_profiles)
    user_query = "Show me salinity profiles near the equator in March 2023"
    response = chat_query(user_query)
    print("AI Response:", response)
    print("Launch interactive Streamlit/Plotly dashboard to visualize calibrated profiles.")


if __name__ == "__main__":
    main()

