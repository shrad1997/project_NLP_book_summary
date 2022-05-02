import streamlit as st
#from googletrans import Translator
from vaderSentiment.vaderSentiment import  SentimentIntensityAnalyzer
import plotly.graph_objects as go
analyser = SentimentIntensityAnalyzer() # initialize it
#translator = Translator() # initialize

st.title("Sentiment analysis of Book summary")
#st.markdown("These are projects from Artificial Intelligence Movement(AIM) Led by [Boadzie Daniel](http://boadzie.surge.sh/)')
#st.markdown("
#App 1: Multilingual Sentimental Analysis’)
st.write("Sentimental Analysis is a branch of Natural Language Processing which involves the extraction of sentiments in text. The VADER package makes it easy to do Sentimental Analysis")
global vs
# The sentiment analyzer function
def sentiment_analyzer_scores(sentence):
   #trans = translator.translate(sentence).text # extracting   translation text
   score1 = analyser.polarity_scores(sentence) # analyzing the text
   score = score1['compound']
   #return score

  # return score
   if score >= 0.05:
      return "The summary of ' " +Book_name+ "' is positive"
   elif score > -0.5 and score < 0.05:
      return "The summary of ' " +Book_name+ "' is neutral"
   else:
      return "The summary of ' " +Book_name+ "' is negative"
   
 
def vadersentimentanalysis(sentence):
    
    vs = (analyser.polarity_scores(sentence))
   

    negative_per = str(vs['neg']*100)
    neutral_per = str(vs['neu']*100)
    positive_per = str(vs['pos']*100)
    #return "sentence was rated as " +negative_per+ "% Negative"
    #return "sentence was rated as " +neutral_per+ "% Neutral"
    #return "sentence was rated as " +positive_per+ "% Positive"
    
    #The plot
    st.header("Pie chart")
    global fig
    fig = go.Figure(
        go.Pie(
            labels = ['negative %','neutral %','positive %'],
            values = [negative_per,neutral_per,positive_per],
            hoverinfo = "label+percent",
            textinfo = "value"
            ))
   
    st.plotly_chart(fig)
    
    return "compound value is " ,vs['compound']
    #return "Overall sentiment is :" + vs


Book_name = st.sidebar.text_area("Book name")
sentence = st.sidebar.text_area("Summary of book") # we take user input
button = st.sidebar.button("Submit")
if button: # a button for submitting the form
   #st.plotly_chart(fig)
   result = sentiment_analyzer_scores(sentence)
   result_2 = vadersentimentanalysis(sentence)# run our function  on it
   st.balloons() # show some cool animation
   st.success(result) # show result in a Bootstrap panel
   st.success(result_2)
   
   #st.plotly_chart(fig)
   
  
