from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quiz, questions , anskey , result
from registration.models import usertype



def quiz(request , quizname):
	user = request.user
	has_email = user.email is not None and user.email != ''
	quiz = questions.objects.filter(inQuiz = quizname)	
	return render(request, 'USER/quiz.html' , {'quiz': quiz , 'name': quizname, 'has_email': has_email })
	

def home(request):
	

	if request.user.is_authenticated:
		user = request.user
		has_email = user.email is not None and user.email != ''
		return redirect('dashboard/')
	else:
		return render(request, 'USER/home.html')

def dashboard(request):
	user = request.user
	has_email = user.email is not None and user.email != ''

	content = {
		'quiz': Quiz.objects.all(),
		'result': result.objects.all(),
		'has_email': has_email
	}
	return render(request, 'USER/dashboard.html' , content)

def prevAns(request):
	user = request.user
	has_email = user.email is not None and user.email != ''
	

	prev = {
		'records': result.objects.filter(username = request.user),
		'anskey' : anskey.objects.filter(username= request.user),
		'has_email': has_email
	}
	return render(request, 'USER/prevAns.html' , prev)

def resultPG(request, quizname):
	quiz = questions.objects.filter(inQuiz = quizname)

	if request.method == 'POST':
		total = 0
		OutOf = 0
		for q in quiz:
			if q.qtype == 'MCQ' or q.qtype == 'TrueFalse':			
				ans = request.POST.get(q.question)
				ofquest = questions.objects.get(question=q.question)
				correctans = q.ansKey1
				if ans == q.ansKey1:
					marks = q.ifCorrect

				elif ans != q.ansKey1 and ans != '':
					marks = q.ifIncorrect
				else:
					marks = 0
				total += marks
				scored = marks
				OutOf += q.ifCorrect


				ak, created = anskey.objects.get_or_create(username=request.user, inQuiz=q.inQuiz , ofQuestion= ofquest)
				if not created:
					anskey.objects.create(username=request.user , inQuiz = q.inQuiz, ofQuestion= ofquest, givenAns1=ans, correctAns= correctans, scored=scored )					
				else:
					ak= anskey.objects.get(username=request.user, inQuiz=q.inQuiz , ofQuestion= ofquest)
					ak.givenAns1=ans
					ak.correctAns=correctans
					ak.scored=scored
					ak.save()
					
					
			elif q.qtype == 'Multiple':
				ans = request.POST.getlist(q.question)
				ofquest = questions.objects.get(question=q.question)
				correctans =  q.ansKey1
				if ans==correctans: 
					marks = q.ifCorrect


				else:
					marks = q.ifIncorrect
				total += marks
				scored = marks
				OutOf += q.ifCorrect

				ak = anskey.objects.get_or_create(username=request.user, inQuiz=q.inQuiz , ofQuestion= ofquest)
				if not created:
					ak.givenAns1 = ans
					ak.correctAns = correctans
					ak.scored = scored
					ak.save()
				else:	
					anskey.objects.create(username=request.user , inQuiz = q.inQuiz, ofQuestion= ofquest, givenAns1=ans, correctAns= correctans, scored=scored )
			anskey.objects.filter(correctAns = None, ofQuestion= q.question).delete()

		inquiz = Quiz.objects.get(quizName = quizname)
		res = result(username =request.user , inQuiz=inquiz,  total= total)
		res.save()

	user = request.user
	has_email = user.email is not None and user.email != ''
		
	supply = {
		'result': result.objects.filter(username= request.user, inQuiz= quizname),
		'anskey': anskey.objects.filter(username= request.user, inQuiz= quizname),
		'outof' : OutOf,
		'total': total,
		'has_email': has_email
		}

	return render(request, 'USER/result.html' , supply )


def addQuestions(request):
	user = request.user
	has_email = user.email is not None and user.email != ''
	if has_email:
		return render(request, 'USER/noaccess.html')
	else:
		if request.method == 'POST':
			qno = request.POST.get('qno')
			question = request.POST.get('question')
			inquiz = request.POST.get('inQuiz')
			qtype = request.POST.get('qtype')
			opt1 = request.POST.get('opt1')
			opt2 = request.POST.get('opt2')
			opt3 = request.POST.get('opt3')
			ans1 = request.POST.get('anskey')
			ans2 = request.POST.get('anskey2')
			ifCorrect = request.POST.get('ifcor')
			ifIncorrect = request.POST.get('ifincor')
			quizn = Quiz.objects.get(quizName = inquiz)

			if ifCorrect == '' and ifIncorrect != '':
				qs = questions(qno=qno, question=question, inQuiz=quizn, qtype=qtype, ansKey1=ans1, ansKey2=ans2,  ifIncorrect=ifIncorrect, opt1=opt1, opt2=opt2, opt3=opt3)
				qs.save()

			elif ifIncorrect == '' and ifCorrect!= '':
				qs = questions(qno=qno, question=question, inQuiz=quizn, qtype=qtype, ansKey1=ans1, ansKey2=ans2, ifCorrect=ifCorrect , opt1=opt1, opt2=opt2, opt3=opt3)
				qs.save()

			elif ifCorrect=='' and ifIncorrect=='':
				qs = questions(qno=qno, question=question, inQuiz=quizn, qtype=qtype, ansKey1=ans1, ansKey2=ans2, opt1=opt1, opt2=opt2, opt3=opt3)
				qs.save()
			else:
				qs = questions(qno=qno, question=question, inQuiz=quizn, qtype=qtype, ansKey1=ans1, ansKey2=ans2, ifCorrect=ifCorrect , ifIncorrect=ifIncorrect, opt1=opt1, opt2=opt2, opt3=opt3)
				qs.save()

			
		return render(request, 'USER/addQuestions.html' ,{'quiz': Quiz.objects.all() , 'has_email': has_email})
	



def addquiz(request):
	user = request.user
	has_email = user.email is not None and user.email != ''
	#'has_email': has_email
	if has_email:
		return render(request, 'USER/noaccess.html')
	else:	
		if request.method == 'POST':
			inquiz=request.POST.get('inQuiz')
			qz = Quiz(quizName=inquiz)
			qz.save()
			
		return render(request, 'USER/addquiz.html' , {'has_email': has_email})

	