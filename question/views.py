from question.models import Question
from quiz.models import Quiz
from question.serializer import QuestionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from validator.validator import validate


@api_view(['GET'])
def QuestionById(request, question_id):
    """
    Get a Question by question_id
    """
    if request.method == 'GET':
        try:
            question = Question.objects.get(pk=question_id)
            serializer = QuestionSerializer(question,)
            return Response(serializer.data,status=201)
        except Question.DoesNotExist as dne:
            return Response({}, status=404)
        except Exception as e:
            response = {
                "status":"failure",
                "reason":str(e)
            }
            return Response(response, status=400)


@api_view(['POST'])
def QuestionSave(request,):
    """
    Create a Question with validation
    """
    if request.method == 'POST':
        data = request.data
        rules = {
            'name': 'required',
            'options': 'required',
            'correct_option': ['integer','required'],
            'quiz': ['integer','required'],
            'points': ['integer','required'],
        }

        validation_result, _, errors= validate(data,rules,return_info=True)
        if validation_result:
            try:
                quiz = Quiz.objects.get(pk=data['quiz'])

                question = Question()
                question.name = data['name']
                question.options = data['options']
                question.correct_option = data['correct_option']
                question.quiz = quiz
                question.points = data['points']
                question.save()

                response = QuestionSerializer(question,).data
                return Response(response, status=201)
            except Exception as e:
                response = {
                    "status": "failure",
                    "reason": str(e)
                }
                return Response(response, status=400)
        else:
            response = {
                "status" : "failure",
                "reason":errors
            }
            return Response(response, status=400)




