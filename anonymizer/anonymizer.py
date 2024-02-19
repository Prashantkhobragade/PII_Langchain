import re
import logging
import spacy
from faker import Faker
from langchain_experimental.data_anonymizer import PresidioReversibleAnonymizer
import pprint
import streamlit as st

import os 
import sys
from logger import logging
from exception import AnnommazationException



# Download and load Spacy model
try:
    logging.info("Downloading SpaCy model...")
    import en_core_web_lg

    nlp = en_core_web_lg.load()
except AnnommazationException as e:
    logging.error(f"Error downloading SpaCy model: {str(e)}")
    raise (e,sys)


anonymizer = PresidioReversibleAnonymizer(add_default_faker_operators=False)

def print_colored_pii(string):
    """
    Print PII (Personally Identifiable Information) colored in red.
    """
    colored_string = re.sub(
        r"(<[^>]*>)", lambda m: "\033[31m" + m.group(1) + "\033[0m", string
    )
    print(colored_string)
    st.markdown(colored_string, unsafe_allow_html=True)
    
def anonymize_pii(document_content):
    try:
        logging.info("Anonymizing starting...")
        """
        Anonymize personally identifiable information in the document content.
        """
        anonymized_content = anonymizer.anonymize(document_content)
        return anonymized_content

        logging.info("Anonymizing completed...")
    
    except Exception as e:
        raise AnnommazationException(e, sys)
    
    
def main():
    
    st.title("PII Anonymizer")

    document_content = st.text_area("Enter document content: ")
    
    if st.button("Anonymize" ):
        if document_content:
            try:
                anonymized_content = anonymize_pii(document_content)
                print_colored_pii(anonymized_content)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                logging.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter document content.")


if __name__ == "__main__":
    main()