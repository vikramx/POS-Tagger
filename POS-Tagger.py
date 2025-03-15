import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

def postagger(text):
  token=word_tokenize(text)
  pos_token=nltk.pos_tag(token)
  return pos_token

def extract_words(pos_tags):
  noun_count=0
  verb_count=0
  adj_count=0

  noun_tag=["NN","NNP","NNS","NNPS"]
  verb_tag=["VB","VBD","VBG","VBN","VBP","VBZ"]
  adj_tag=["JJ","JJR","JJS"]

  for i,j in pos_tags:
    if j in noun_tag:
      noun_count+=1
    elif j in verb_tag:
      verb_count+=1
    elif j in adj_tag:
      adj_count+=1

    ans=[noun_count,verb_count,adj_count]
  return ans

def visualise(word_count):
    fig,ax=plt.subplots()
    x=["Nouns","Verbs","Adjectives"]
    ax.bar(x,word_count,color=['r','g','b'])
    ax.set_xlabel("Parts Of Speech")
    ax.set_ylabel("Counts")
    ax.set_title("POS Word Counts")
    st.pyplot(fig)


st.title("POS Tagged Words")
st.write("Enter text to analyse the nouns,adjectives and verbs in it.")

data=st.text_area("Enter text here:")

if st.button("Analyse"):
    tags=postagger(data)
    words=extract_words(tags)

    st.write("POS Tagged Words:")
    st.write(tags)

    st.write("Word Count")
    st.write(f"Nouns:{words[0]}\n Verbs:{words[1]}\n Adjectives:{words[2]}\n")

    visualise(words)
