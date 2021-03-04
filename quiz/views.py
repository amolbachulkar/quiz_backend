from quiz.models import Quiz
from quiz.serializer import QuizSerializer
from question.models import Question
from question.serializer import QuestionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from validator.validator import validate


@api_view(['GET',])
def QuizById(request, quiz_id):
    """
    Get a quiz by quiz_id
    """
    if request.method == 'GET':
        try:
            quiz = Quiz.objects.get(pk=quiz_id)
            serializer = QuizSerializer(quiz,)
            return Response(serializer.data,status=201)
        except Quiz.DoesNotExist as dne:
            return Response({}, status=404)
        except Exception as e:
            response = {
                "status":"failure",
                "reason":str(e)
            }
            return Response(response, status=400)


@api_view(['POST'])
def QuizSave(request,):
    """
    Create a quiz with validations
    """
    if request.method == 'POST':
        data = request.data
        rules = {
            'name': 'required',
            'description': 'required'
        }
        validation_result, _, errors= validate(data,rules,return_info=True)
        if validation_result:
            try:
                quiz = Quiz(name=data['name'], description=data['description'])
                quiz.save()
                response = QuizSerializer(quiz,).data
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


@api_view(['GET',])
def QuizQuestions(request, quiz_id):
    """
    Get all questions for a quiz.
    """
    if request.method == 'GET':
        try:
            quiz = QuizSerializer(Quiz.objects.get(pk=quiz_id)).data
            questions = QuestionSerializer(Question.objects.filter(quiz=quiz_id), many=True).data
            quiz['questions'] =questions
            return Response(quiz,status=201)
        except Quiz.DoesNotExist as dne:
            return Response({}, status=404)
        except Exception as e:
            response = {
                "status":"failure",
                "reason":str(e)
            }
            return Response(response, status=400)
