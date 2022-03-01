#from dbconnection import get_database
#from dbinsert import addMany

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

def insertCollections():
    for i in range (len(collectionList)):
        print(collectionList[i][0])
        #collectionname = collectionList[i][0]
        #newcollection = dbname[collectionname]

#if __name__ == "__main__": 
#dbname = get_database() 
#addMany()
insertCollections()