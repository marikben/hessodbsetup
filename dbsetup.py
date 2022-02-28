collectionList = [["Tags", "_idQuestionMotif", "textQuestion", "_idTags", "texteReponse"],
["QuestionParaVitaux", "_idQuestionParaVitaux", "textQuestion", "_idTags", "texteReponse"],
["QuestionAnamnese", "_idQuestionAnamnese", "textQuestion", "_idTags", "texteReponse"],
["QuestionMotif", "_idQuestionMotif", "textQuestion", "_idTags", "texteReponse"],
["Patient", "_idPatient", "description", "genre", "age", "_idSigneVitaux", "_idQuestionParaVitaux",
 "_idQuestionAnamnese", "_idMotif", "_idQuestionMotif"],
["Motif", "_idMotif", "description", "_idDegrees", "_idConditions", "_idParamVitaux"],
["Degree", "_idDegrees", "degree"],
["Condition", "_idCondition", "_idMotif", "_idDegrees", "textQuestion"],
["SigneVitaux", "_idSigneVitaux", "glasgow", "_idPupilles", "pulsation", "tas",
 "tad", "spo2", "peakflowMin", "peakflowCM", "glycemie", "frequenceRespiratoire",
  "cetonemie", "douleur"], ["Pupilles", "_idPupilles", "pupilleReact", "pupilleSecondaire"]]

def insertCollections(){
    #tähän testaat että saatko ekan arvon eli nimen tulostettua
}
if __name__ == "__main__":    


   print(len(collectionList))