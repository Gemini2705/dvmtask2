from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
	quizName = models.CharField(max_length= 100, primary_key=True)
	

class questions(models.Model):
	qno = models.IntegerField()
	question = models.TextField(primary_key=True)
	inQuiz = models.ForeignKey(Quiz, to_field='quizName',  on_delete=models.CASCADE)
	opt1 = models.CharField(max_length = 50)
	opt2 = models.CharField(max_length = 50)
	opt3 = models.CharField(max_length = 50)
	qtype = models.CharField(max_length = 15) #can be MCQ , TrueFalse , Multiple
	ifCorrect = models.IntegerField(default = 4)
	ifIncorrect = models.IntegerField(default = -1)
	ansKey1 = models.TextField()

class anskey(models.Model):
	username = models.ForeignKey(User, to_field= 'username', on_delete=models.CASCADE)
	inQuiz = models.ForeignKey(Quiz,to_field= 'quizName' , on_delete=models.CASCADE)
	ofQuestion = models.ForeignKey(questions, to_field= 'question' , on_delete=models.CASCADE)
	givenAns1 = models.TextField(null= True , default=None)
	correctAns = models.TextField(null= True , default=None)
	scored = models.IntegerField(null= True , default=None)

class result(models.Model):
	username = models.ForeignKey(User, to_field= 'username' , on_delete=models.CASCADE)
	inQuiz = models.ForeignKey(Quiz,to_field='quizName' , on_delete=models.CASCADE)
	marks = models.IntegerField(null= True , default=None)
	total = models.IntegerField()