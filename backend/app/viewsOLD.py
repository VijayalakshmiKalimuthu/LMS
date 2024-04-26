from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import appinfo,course_schedule, course_content_feedback, attendance_master, announcement_master, trainer_skill_map, trainer_availability, test_question_map,skill_type,login,tests_candidates_answers,tests_candidates_map,content_detail,course_candidates_map,college_admin,test_master,course_contents,question_master,candidate_master,content_master,skills_master,courses_master,topic_master,test_type,question_type,college_master,department_master,trainer_master
from .serializers import loginSerializer,appinfoSerializer,tests_candidates_answerSerializer,courseScheduleSerializer, courseContentFeedbackSerializer, attendanceMasterSerializer, announcementSerializer, trainerSkillMapSerializer, trainerAvailabilitySerializer, testQuestionMapSerializer,testcandidatemapSerializers,contentdetailSerializer,coursecandidatesmapSerializer,collegeadminSerializers,coursecontentsSerializer,testsSerializers,questionsSerializer,skilltypeSerializer,contentSerializers,collegeSerializers,departmentSerializers,questiontypeSerializers,testtypeSerializers,topicSerializers,courseSerializer,skillSerializer,candidatesSerializer,trainerSerializer, testsSerializersImport, questionsSerializerImport
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd

# Create your views here.
class appinfogetAPIView(generics.ListAPIView):
    queryset = appinfo.objects.all()

    
    serializer_class = appinfoSerializer


class appinfoAPIView(generics.CreateAPIView):
    queryset = appinfo.objects.all()
    serializer_class = appinfoSerializer

class appinfoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = appinfo.objects.all()
    serializer_class = appinfoSerializer
#_____________________________Master Tables_____________________________________________#

class skilltypegetAPIView(generics.ListAPIView):
    queryset = skill_type.objects.all()

    
    serializer_class = skilltypeSerializer


class skilltypecreateAPIView(generics.CreateAPIView):
    queryset = skill_type.objects.all()
    serializer_class = skilltypeSerializer

class skilltypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateAPIView):
    queryset = skill_type.objects.all()
    serializer_class = skilltypeSerializer

@api_view(['PUT', 'PATCH'])
def delete_skill_type(request, pk):
    try:
        print("Entering Function..")
        skilltype = skill_type.objects.get(id=pk)

        print("skilltyp: ", skilltype)
    except skill_type.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    skilltype.deleted = 1
    skilltype.save()
    print("skilltype: ", skilltype)

    return JsonResponse("skill 'deleted' field updated successfully", safe=False)


#------------------------------Test-type-------------------------------------------------------------#


class test_type_listView(generics.ListAPIView):
    queryset = test_type.objects.all()

    
    serializer_class = testtypeSerializers

class test_type_create(generics.CreateAPIView):
    queryset = test_type.objects.all()
    serializer_class = testtypeSerializers

class test_type_Update(generics.RetrieveUpdateAPIView):
    queryset = test_type.objects.all()
    serializer_class = testtypeSerializers

@api_view(['PUT', 'PATCH'])
def delete_test_type(request, pk):
    try:
        print("Entering Function..")
        test_typevar = test_type.objects.get(id=pk)

       
    except test_type.DoesNotExist:
        return JsonResponse("test_type not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    test_typevar.deleted = 1
    test_typevar.save()
 

    return JsonResponse("test_type 'deleted' field updated successfully", safe=False)

#------------------------------------Question_type--------------------------------------#

class question_type_listView(generics.ListAPIView):
    serializer_class = questiontypeSerializers

    def get_queryset(self):
        if self.request.method == 'GET':
            return question_type.objects.all()
        return question_type.objects.all()

class question_type_create(generics.CreateAPIView):
    queryset = question_type.objects.all()
    serializer_class = questiontypeSerializers

class question_type_Update(generics.RetrieveUpdateAPIView):
    queryset = question_type.objects.all()
    serializer_class = questiontypeSerializers

@api_view(['PUT', 'PATCH'])
def delete_question_type(request, pk):
    try:
        print("Entering Function..")
        question_typevar = question_type.objects.get(id=pk)

       
    except question_type.DoesNotExist:
        return JsonResponse("question_type not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    question_typevar.deleted = 1
    question_typevar.save()
 

    return JsonResponse("question_type 'deleted' field updated successfully", safe=False)


#------------------------------college----------------------------------------#


class CollegeListView(generics.ListAPIView):
    serializer_class = collegeSerializers

    def get_queryset(self):
        return college_master.objects.all()

class collegeCreateView(generics.CreateAPIView):
    queryset = college_master.objects.all()
    serializer_class = collegeSerializers

class collegeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = college_master.objects.all()
    serializer_class = collegeSerializers

@api_view(['PUT', 'PATCH'])
def delete_college(request, pk):
    try:
        college = college_master.objects.get(id=pk)
    except college_master.DoesNotExist:
        return Response("college not found", status=404)

    college.deleted = 1
    college.save()

    return Response("college 'deleted' field updated successfully")

#----------------------------------------department---------------------------------------------#

class DepartmentListView(generics.ListAPIView):
    serializer_class = departmentSerializers

    def get_queryset(self):
        return department_master.objects.all()

class departmentCreateView(generics.CreateAPIView):
    queryset = department_master.objects.all()
    serializer_class = departmentSerializers

class departmentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = department_master.objects.all()
    serializer_class = departmentSerializers

@api_view(['PUT', 'PATCH'])
def delete_department(request, pk):
    try:
        department = department_master.objects.get(id=pk)
    except department_master.DoesNotExist:
        return Response("department not found", status=404)

    department.deleted = 1
    department.save()

    return Response("department 'deleted' field updated successfully")


#__________________________topic_master___________________________________#


class topicListView(generics.ListAPIView):
    serializer_class = topicSerializers

    def get_queryset(self):
        return topic_master.objects.all()

class topicCreateView(generics.CreateAPIView):
    queryset = topic_master.objects.all()
    serializer_class = topicSerializers

class topicUpdateView(generics.RetrieveUpdateAPIView):
    queryset = topic_master.objects.all()
    serializer_class = topicSerializers

@api_view(['PUT', 'PATCH'])
def delete_topic(request, pk):
    try:
        topic = topic_master.objects.get(id=pk)
    except topic_master.DoesNotExist:
        return Response("topic not found", status=404)

    topic.deleted = 1
    topic.save()

    return Response("topic 'deleted' field updated successfully")
#___________________________SKILL_master_________________________________________

@api_view(['GET'])
def get_skills(request):
    skills = skills_master.objects.all()  # Accessing the skill model directly
    
    skill_data = []
    for skillset in skills:
        skill_type_id = None
        if skillset.skill_type_id:
            skill_type_id= skillset.skill_type_id.skill_type
            skill_data.append({
                'id': skillset.id,
                'skill_name': skillset.skill_name,
                'skill_type_id': skill_type_id,
            })
    return Response(skill_data)

class skillscreateAPIView(generics.CreateAPIView):
    queryset = skills_master.objects.all()
    serializer_class = skillSerializer

class skillsRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = skills_master.objects.all()
    serializer_class = skillSerializer

@api_view(['PUT', 'PATCH'])
def delete_skills(request, pk):
    try:
        print("Entering Function..")
        skills = skills_master.objects.get(id=pk)

        print("skill: ", skills)
    except skills_master.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    skills.deleted = 1
    skills.save()
    print("skill: ", skills)

    return JsonResponse("skill 'deleted' field updated successfully", safe=False)


#_________________________Courses_master______________________________________



@api_view(['GET'])
def get_course(request):
    courseset=courses_master.objects.all()
   
    course_data=[]
    for courses in  courseset:
       
        topic_id=None
        skill_id=None
       
        if courses.topic_id:
           topic_id=courses.topic_id.topic 
        if courses.skill_id:
           skill_id=courses.skill_id.skill_name
          
        course_data.append({
               'id': courses.id,
            'course_name': courses.course_name,
           
            'topic_id':topic_id,
            'skill_id':skill_id,
            'dtm_start': courses.dtm_start,
            'dtm_end': courses.dtm_end,
           
            'course_count': courses.course_count,
            
            'total_enrollment': courses.total_enrollment,
            'is_active':courses.is_active,
           
       
          

            })
    return Response(course_data)



class coursecreateAPIView(generics.CreateAPIView):
    queryset = courses_master.objects.all()
    serializer_class =courseSerializer

class courseUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = courses_master.objects.all()
    serializer_class =courseSerializer

@api_view(['PUT', 'PATCH'])
def delete_course(request, pk):
    try:
        print("Entering Function..")
        course=courses_master.objects.get(id=pk)

        print("course: ",course)
    except courses_master.DoesNotExist:
        return JsonResponse("courses not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    course.deleted = 1
    course.save()
    print("course: ",course)

    return JsonResponse("course 'deleted' field updated successfully", safe=False)

#___________________________________candidate_master________________________________________
@api_view(['GET'])
def get_candidate(request):
    candidatelist=candidate_master.objects.all()
   
    candidate_data=[]
    for candidate in  candidatelist:
        college_id=None
       
        department_id=None
      
        if candidate.college_id:
           college_id=candidate.college_id.college
      
        if candidate.department_id:
           department_id=candidate.department_id.department
        
       
           candidate_data.append({
              'id': candidate.id,
               'college_id': college_id,
              'students_name':candidate.students_name,
            
            'registration_number':candidate.registration_number,
            'gender':candidate.gender,
           
            'email_id':candidate.email_id,
            'mobile_number':candidate.mobile_number,
            'year':candidate.year,
            'cgpa':candidate.cgpa,
            'department_id': department_id,
            'marks_10th':candidate.marks_10th,
            'marks_semester_wise':candidate.marks_semester_wise,
            'history_of_arrears':candidate. history_of_arrears,
            'standing_arrears':candidate.standing_arrears,
            'number_of_offers':candidate.number_of_offers



            })
    return Response(candidate_data)


class candidatescreateAPIView(generics.CreateAPIView):
    queryset = candidate_master.objects.all()
    serializer_class = candidatesSerializer

class candidates_Select_Update(generics.RetrieveUpdateAPIView):
    queryset = candidate_master.objects.all()
    serializer_class = candidatesSerializer

@api_view(['PUT', 'PATCH'])
def delete_candidates(request, pk):
    try:
        print("Entering Function..")
        trainees = candidate_master.objects.get(id=pk)

        print("tests: ", trainees)
    except candidate_master.DoesNotExist:
        return JsonResponse("trainees not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    trainees.deleted = 1
    trainees.save()
    print("tests: ", trainees)

    return JsonResponse("trainees 'deleted' field updated successfully", safe=False)

#____________________________________content_master________________________________________
@api_view(['GET'])
def get_content(request):
    contentlist=content_master.objects.all()
   
    content_data=[]
    for content in  contentlist:
        topic_id=None
       
       # sub_topic_id=None
      
        if content.topic_id:
           topic_id=content.topic_id.topic
      
       # if content.sub_topic_id:
        #   sub_topic_id=content.sub_topic_id.sub_topic
        
       
           content_data.append({
              'id': content.id,
               'topic_id': topic_id,
              'content_type':content.content_type,
            
            'content_url':content.content_url,
            'actual_content':content.actual_content,
           
            'status':content.status,
            'added_by':content.added_by,
            'size':content.size,
            'guidelines':content.guidelines,
           # 'sub_topic_id': sub_topic_id,
            'dtm_active_from':content.dtm_active_from,
            'dtm_validity':content.dtm_validity,
            'feedback':content.feedback,
          


            })
    return Response(content_data)




class contentcreateAPIView(generics.CreateAPIView):
    queryset = content_master.objects.all()
    serializer_class =contentSerializers

class contentUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = content_master.objects.all()
    serializer_class =contentSerializers

@api_view(['PUT', 'PATCH'])
def delete_content(request, pk):
    try:
        print("Entering Function..")
        content=content_master.objects.get(id=pk)

        print("content: ",content)
    except content_master.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    content.deleted = 1
    content.save()
    print("content: ",content)

    return JsonResponse("content 'deleted' field updated successfully", safe=False)
#_______________________________________trainer_master__________________________________________________________


class TrainerListAPIView(generics.ListAPIView):
    queryset = trainer_master.objects.all()
    serializer_class = trainerSerializer

class TrainerCreateAPIView(generics.CreateAPIView):
    queryset = trainer_master.objects.all()
    serializer_class = trainerSerializer

class TrainerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = trainer_master.objects.all()
    serializer_class = trainerSerializer

@api_view(['PUT', 'PATCH'])
def delete_trainer(request, pk):
    try:
        print("Entering Function..")
        trainer=trainer_master.objects.get(id=pk)

        print("trainer: ",trainer)
    except trainer_master.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    trainer.deleted = 1
    trainer.save()
    print("content: ",trainer)

    return JsonResponse("trainer 'deleted' field updated successfully", safe=False)



#_____________________________________Test_________________________________________________________#



@api_view(['GET'])
def get_test(request):
    testset=test_master.objects.all()
   
    test_data=[]
    for test in  testset:
        test_type_id = None
        question_type_id = None  # Initialize question_type variable
        college_id=None
        department_id=None
       
        course_id=None
        if test.test_type_id:
           test_type_id=test.test_type_id.test_type
      
        if test.question_type_id:
           question_type_id=test.question_type_id.question_type
        if test.college_id:
           college_id=test.college_id.college
      
        if test.department_id:
           department_id=test.department_id.department
       
        if test.course_id:
           course_id=test.course_id.course_name
          
        test_data.append({
               'id': test.id,
            'test_name': test.test_name,
            'test_type_id': test_type_id,
            'question_type_id': question_type_id,  # Add question_type field to the response
            'students_count': test.students_count,
           
            'course_id':course_id,
            'dtm_start': test.dtm_start,
            'dtm_end': test.dtm_end,
            'college_id': college_id,
            'duration': test.duration,
            'year': test.year,
            'rules': test.rules,
           
            'department_id': department_id,
            'need_candidate_info': test.need_candidate_info
       
       
          

            })
    return Response(test_data)

class testcreateAPIView(generics.CreateAPIView):
    queryset = test_master.objects.all()
    serializer_class = testsSerializers

class testsRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = test_master.objects.all()
    serializer_class = testsSerializers

#class testsRetrievedeleteAPIView(generics.DestroyAPIView):
   # queryset = tests_master.objects.all()
   # serializer_class = testsSerializers

@api_view(['PUT', 'PATCH'])
def delete_tests(request, pk):
    try:
        print("Entering Function..")
        test = test_master.objects.get(id=pk)

      
    except test_master.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    test.deleted = 1
    test.save()
    print("skill1: ",test)

    return JsonResponse("skill 'deleted' field updated successfully", safe=False)
#______________________________________Question_master________________________________________
@api_view(['GET'])
def get_questions(request):
    questionset=question_master.objects.all()
   
    question_data=[]
    for question in  questionset:
        question_type_id=None
        topic_id=None
        skill_id=None
      
        if question.question_type_id:
           question_type_id=question.question_type_id.question_type
        if question.skill_id:  
           skill_id=question.skill_id.skill_name
        if question.topic_id:
           topic_id=question.topic_id.topic
           question_data.append({
              'id': question.id,
              'question_name':question.question_name,
              'question_text':question.question_text,
              'option_a':question.option_a,
              'option_b':question.option_b,
              'option_c':question.option_c,
              'option_d':question.option_d,
              'option_e':question.option_e,
              'option_f':question.option_f,
              'skill_id':skill_id,
              'view_hint':question.view_hint,
              'mark':question.mark,
              'explain_answer':question.explain_answer,
             'topic_id':topic_id,
              'question_type_id':question_type_id,
              'answer':question.answer,
              'negative_mark':question.negative_mark,


            })
    return Response(question_data)
class questionscreateAPIView(generics.CreateAPIView):
    queryset = question_master.objects.all()
    serializer_class = questionsSerializer

class questionsRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = question_master.objects.all()
    serializer_class = questionsSerializer 

@api_view(['PUT', 'PATCH'])
def delete_question(request, pk):
    try:
        print("Entering Function..")
        question = question_master.objects.get(id=pk)

        print("skill: ", question)
    except question_master.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    question.deleted = 1
    question.save()
    print("skill: ", question)

    return JsonResponse("skill 'deleted' field updated successfully", safe=False)
#_______________________________________COLLEGE_admin____________________


@api_view(['GET'])
def get_collegeadmin(request):
    adminset = college_admin.objects.all()  # Accessing the skill model directly
    
    skill_data = []
    for admin in adminset:
        college_id = None
        if admin.college_id:
            college_id= admin.college_id.college_id
            skill_data.append({
                'admin_name': admin.admin_name,
                'college_id': college_id,
            })
    return Response(skill_data)

class collegeadmincreateAPIView(generics.CreateAPIView):
    queryset = college_admin.objects.all()
    serializer_class = collegeadminSerializers

class collegeadminRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = college_admin.objects.all()
    serializer_class = collegeadminSerializers

@api_view(['PUT', 'PATCH'])
def delete_college_admin(request, pk):
    try:
        print("Entering Function..")
        college_ad = college_admin.objects.get(id=pk)

       
    except college_admin.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    college_ad.deleted = 1
    college_ad.save()
   

    return JsonResponse("collegeadmin 'deleted' field updated successfully", safe=False)


#__________________________course_contents____________________________________#


@api_view(['GET'])
def get_course_content(request):
    coursecntent=course_contents.objects.all()

    print('Course Content:', coursecntent)
   
    content_course_data=[]
    for contents in  coursecntent:
        print('contents: ', contents)
        
        course_id=None
        content_id=None
        topic_id=None
        sub_topic=None
       
        if contents.content_id:
           content_id=contents.content_id.content_url
       
        if contents.course_id:
           course_id=contents.course_id.course_name
        
        if contents.topic_id:
           topic_id=contents.topic_id.topic
       
        sub_topic = contents.topic_id.sub_topic if contents.topic_id and contents.topic_id.sub_topic else None
       # if contents.sub_topic_id:
       #   sub_topic_id=contents.sub_topic_id.sub_topic
      
       
        content_course_data.append({
            'id':contents.id,
            
            'content_id':content_id,
            'course_id':course_id,
            'topic':topic_id,
            'sub_topic': sub_topic,
           
              })
    return Response(content_course_data)



class coursecontentscreateAPIView(generics.CreateAPIView):
    queryset = course_contents.objects.all()
    serializer_class =coursecontentsSerializer

class coursecontentsUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = course_contents.objects.all()
    serializer_class =coursecontentsSerializer
@api_view(['PUT', 'PATCH'])
def delete_course_contents(request, pk):
    try:
        print("Entering Function..")
        contents=course_contents.objects.get(id=pk)

       
    except course_contents.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    contents.deleted = 1
    contents.save()
   

    return JsonResponse("tests_result 'deleted' field updated successfully", safe=False)


#_______________________course_candidates_map______________________________



@api_view(['GET'])
def get_course_candidates_map(request):
    coursecan=course_candidates_map.objects.all()
   
    course_map_data=[]
    for content in  coursecan:
         # Initialize question_type variable
        course_id=None
        student_id=None
        college_id=None
        if content.college_id:
            college_id= content.college_id.college
       
        if content.student_id:
           student_id=content.student_id.student_name
       
        if content.course_id:
           course_id=content.course_id.course_name
      
       
        course_map_data.append({
               'id':content.id,
               
               
             # Add question_type field to the response
            'student_id':student_id,
            'course_id':course_id,
            'collge_id':college_id,
            'dt_enrolled':content.dt_enrolled,
            'dt_validity':content.dt_validity,
            'status':content.status,
           
              })
    return Response(course_map_data)



class coursecandidatesmapcreateAPIView(generics.CreateAPIView):
    queryset = course_candidates_map.objects.all()
    serializer_class =coursecandidatesmapSerializer

class coursecandidatesmapUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = course_candidates_map.objects.all()
    serializer_class =coursecandidatesmapSerializer
@api_view(['PUT', 'PATCH'])
def delete_course_can(request, pk):
    try:
        print("Entering Function..")
        contnt=course_candidates_map.objects.get(id=pk)

       
    except course_candidates_map.DoesNotExist:
        return JsonResponse("candidate map for course not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    contnt.deleted = 1
    contnt.save()
   

    return JsonResponse("candidate map 'deleted' field updated successfully", safe=False)


#_________________________________content_detail_______________________________________________________________#

@api_view(['GET'])
def get_content_detail(request):
    cntent=content_detail.objects.all()
   
    contents_data=[]
    for contentsdetail in  cntent:
         # Initialize question_type variable
       
        content_id=None
        
       
        if contentsdetail.content_id:
           content_id=contentsdetail.content_id.content_url
       
       
       
        contents_data.append({
               'id':contentsdetail.id,
             # Add question_type field to the response
            'content_id':content_id,
           
            'actual_content':contentsdetail.actual_content,
            'status':contentsdetail.status,
            'content_url':contentsdetail.content_url
           
              })
    return Response(contents_data)



class contentdetailcreateAPIView(generics.CreateAPIView):
    queryset = content_detail.objects.all()
    serializer_class =contentdetailSerializer

class coursecontentdetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = content_detail.objects.all()
    serializer_class =contentdetailSerializer
@api_view(['PUT', 'PATCH'])
def delete_content_detail(request, pk):
    try:
        print("Entering Function..")
        contentdtil=content_detail.objects.get(id=pk)

       
    except content_detail.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    contentdtil.deleted = 1
    contentdtil.save()
   

    return JsonResponse("tests_result 'deleted' field updated successfully", safe=False)



#____________________________test_candidate-map________________________________#
@api_view(['GET'])
def get_tests_candidates_map(request):
    tests_candidates=tests_candidates_map.objects.all()
   
    test_candidate_map_data=[]
    for testing in  tests_candidates:
        test_id = None
        question_id= None  # Initialize question_type variable
        student_id=None
        college_id=None
        department_id=None
        if testing.test_id:
           test_id=testing.test_id.test_name
        if testing.department_id:
           department_id=testing.department_id.department
      
        if testing.question_id:
           question_id=testing.question_id.question_name
        if testing.student_id:
           student_id=testing.student_id.students_name
        if testing.college_id:
            college_id= testing.college_id.college
       
        test_candidate_map_data.append({
            'id': testing.id,
            'test_id':test_id,
            'college_id':college_id,
            'department_id':department_id,
            'question_id':question_id,  # Add question_type field to the response
            'student_id':student_id,
            'dtm_start': testing.dtm_start,
            'dtm_end': testing.dtm_end,
            'dtm_schedule1_start':testing.dtm_schedule1_start,
            'dtm_schedule1_end': testing.dtm_schedule1_end,
            'dtm_schedule2_start': testing.dtm_schedule2_start,
            'dtm_schedule2_end': testing.dtm_schedule2_end,
            'attempt_count':testing.attempt_count,
           'is_actual_test':testing.is_actual_test,
            'is_active': testing.is_active,
            'duration':testing.duration,
            'year':testing.year,
            'rules':testing.rules,
            'need_candidate_info':testing.need_candidate_info
       
       
          

            })
    return Response(test_candidate_map_data)



class testcandidatemapcreateAPIView(generics.CreateAPIView):
    queryset = tests_candidates_map.objects.all()
    serializer_class =testcandidatemapSerializers

class testcandidatemapUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = tests_candidates_map.objects.all()
    serializer_class =testcandidatemapSerializers

@api_view(['PUT', 'PATCH'])
def delete_testcandidatemap(request, pk):
    try:
        print("Entering Function..")
        tests_candidates=tests_candidates_map.objects.get(id=pk)

        print("tests_candidates: ",tests_candidates)
    except tests_candidates_map.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    tests_candidates.deleted = 1
    tests_candidates.save()
    print("tests_candidates: ",tests_candidates)

    return JsonResponse("tests_candidates_map 'deleted' field updated successfully", safe=False)

#__________________________test_candidate_answer____________________________
@api_view(['GET'])
def get_tests_candidates_answer(request):
    tests_candidates_ans=tests_candidates_answers.objects.all()
    test_candidate_answer_data=[]
    for testans in  tests_candidates_ans:
         # Initialize question_type variable
        student_id=None
        test_id=None
        question_id=None
        if testans.student_id:
           student_id=testans.student_id.students_name
        
        if testans.test_id:
           test_id=testans.test_id.test_name
        if testans.question_id:
           question_id=testans.question_id.question_text
       
        test_candidate_answer_data.append({
               'id': testans.id,
             # Add question_type field to the response
            'student_id':student_id,
            'question_id':question_id,
            'test_id':test_id,
            'answer': testans.answer,
            'result':testans.result
       
       
          

            })
    return Response(test_candidate_answer_data)



class testcandidateanscreateAPIView(generics.CreateAPIView):
    queryset = tests_candidates_answers.objects.all()
    serializer_class =tests_candidates_answerSerializer

class testcandidateansUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = tests_candidates_answers.objects.all()
    serializer_class =tests_candidates_answerSerializer

@api_view(['PUT', 'PATCH'])
def delete_testcandidatemap(request, pk):
    try:
        print("Entering Function..")
        tests_candidates_ans=tests_candidates_answers.objects.get(id=pk)

        print("tests_candidates_ans: ",tests_candidates_ans)
    except tests_candidates_answers.DoesNotExist:
        return JsonResponse("tests not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    tests_candidates_ans.deleted = 1
    tests_candidates_ans.save()
    print("tests_candidates: ",tests_candidates_ans)

    return JsonResponse("tests_candidates_ans 'deleted' field updated successfully", safe=False)



#-----------------------------Login-----------------------------------------#

class login_create(generics.CreateAPIView):
    queryset = login.objects.all()
    serializer_class = loginSerializer


@api_view(['GET'])
def get_login(request):
    login_set = login.objects.select_related('college_id').all()

    login_data=[]
    for logins in  login_set:
           login_data.append({
              'id': logins.id,
              'email': logins.email,
              'user_name': logins.user_name,
              'password': logins.password,
              'role': logins.role,
              'college_id': logins.college_id.id,
              'college_name': logins.college_id.college
            })
    return Response(login_data)

class update_login(generics.UpdateAPIView):
    queryset = login.objects.all()
    serializer_class = loginSerializer



@api_view(['PUT', 'PATCH'])
def delete_login(request, pk):
    try:
        print("Entering Function..")
        logins = login.objects.get(id=pk)

        print("skilltyp: ", logins)
    except login.DoesNotExist:
        return JsonResponse("login not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    logins.deleted = 1
    logins.save()
    print("logins: ", logins)

    return JsonResponse("logins 'deleted' field updated successfully", safe=False)


#-----------------------------Course Schedule-----------------------------------------#

class add_course_schedule(generics.CreateAPIView):
    queryset = course_schedule.objects.all()
    serializer_class = courseScheduleSerializer


@api_view(['GET'])
def get_course_schedule(request):
    cs_set = course_schedule.objects.select_related('student_id', 'course_id', 'trainer_id').all()

    course_schedule_data=[]
    for cs in  cs_set:
           course_schedule_data.append({
              'id': cs.id,
              'student_id': cs.student_id.students_name,
              'course_id': cs.course_id.course_name,
              'trainer_id': cs.trainer_id.trainer_name,
              'dtm_start': cs.dtm_start,
              'dtm_end': cs.dtm_end,
              'course_mode': cs.course_mode,
              'status': cs.status
            })
    return Response(course_schedule_data)

class update_course_schedule(generics.UpdateAPIView):
    queryset = login.objects.all()
    serializer_class = loginSerializer



@api_view(['PUT', 'PATCH'])
def delete_course_schedule(request, pk):
    try:
        print("Entering Function..")
        course = course_schedule.objects.get(id=pk)

        print("course: ", course)
    except course_schedule.DoesNotExist:
        return JsonResponse("course not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    course.deleted = 1
    course.save()
    print("logins: ", course)

    return JsonResponse("course 'deleted' field updated successfully", safe=False)



#-----------------------------Course Content Feedback-----------------------------------------#

class add_course_content_feedback(generics.CreateAPIView):
    queryset = course_content_feedback.objects.all()
    serializer_class = courseContentFeedbackSerializer


@api_view(['GET'])
def get_course_content_feedback(request):
    course_set = course_content_feedback.objects.select_related('course_id', 'student_id', 'topic_id', 'trainer_id').all()

    course_content_data=[]
    for cc in  course_set:
           course_content_data.append({
              'id': cc.id,
              'course_id': cc.course_id.course_name,
              'student_id': cc.student_id.students_name,
              'topic_id': cc.topic_id.topic,
              'dtm_session': cc.dtm_session,
              'trainer_id': cc.trainer_id.trainer_name,
              'feedback': cc.feedback
            })
    return Response(course_content_data)

class update_course_content_feedback(generics.UpdateAPIView):
    queryset = course_content_feedback.objects.all()
    serializer_class = courseContentFeedbackSerializer



@api_view(['PUT', 'PATCH'])
def delete_course_content_feedback(request, pk):
    try:
        print("Entering Function..")
        course = course_content_feedback.objects.get(id=pk)

        print("course: ", course)
    except course_content_feedback.DoesNotExist:
        return JsonResponse("course not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    course.deleted = 1
    course.save()
    print("course: ", course)

    return JsonResponse("course 'deleted' field updated successfully", safe=False)


#-----------------------------Attendance Master-----------------------------------------#

class add_attendance_master(generics.CreateAPIView):
    queryset = attendance_master.objects.all()
    serializer_class = attendanceMasterSerializer


@api_view(['GET'])
def get_attendance_master(request):
    attend_set = attendance_master.objects.select_related('student_id', 'course_id', 'test_id').all()

    attendance_data=[]
    for attend in  attend_set:
           attendance_data.append({
              'id': attend.id,
              'student_id': attend.student_id.students_name,
              'course_id': attend.course_id.course_name,
              'test_id': attend.test_id.test_name,
              'dtm_attendance': attend.dtm_attendance
            })
    return Response(attendance_data)

class update_attendance_master(generics.UpdateAPIView):
    queryset = attendance_master.objects.all()
    serializer_class = attendanceMasterSerializer



@api_view(['PUT', 'PATCH'])
def delete_attendance_master(request, pk):
    try:
        print("Entering Function..")
        attend = attendance_master.objects.get(id=pk)

        print("attend: ", attend)
    except attendance_master.DoesNotExist:
        return JsonResponse("course not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    attend.deleted = 1
    attend.save()
    print("attend: ", attend)

    return JsonResponse("attend 'deleted' field updated successfully", safe=False)



#-----------------------------Announcement Master-----------------------------------------#

class add_announcement_master(generics.CreateAPIView):
    queryset = announcement_master.objects.all()
    serializer_class = announcementSerializer


@api_view(['GET'])
def get_announcement_master(request):
    announce_set = announcement_master.objects.select_related('college_id', 'trainer_id').all()

    announce_data=[]
    for announce in announce_set:
        announce_data.append({
            'id': announce.id,
            'college_id': announce.college_id.college_name,
            'trainer_id': announce.trainer_id.trainer_name,
            'dtm_start': announce.dtm_start,
            'dtm_end': announce.dtm_end,
            'content': announce.content,
            'is_active': announce.is_active
        })
    return Response(announce_data)

class update_announcement_master(generics.UpdateAPIView):
    queryset = announcement_master.objects.all()
    serializer_class = announcementSerializer



@api_view(['PUT', 'PATCH'])
def delete_announcement_master(request, pk):
    try:
        print("Entering Function..")
        announce = announcement_master.objects.get(id=pk)

        print("announce: ", announce)
    except announcement_master.DoesNotExist:
        return JsonResponse("announce not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    announce.deleted = 1
    announce.save()
    print("announce: ", announce)

    return JsonResponse("announce 'deleted' field updated successfully", safe=False)


#-----------------------------Trainer Skill Map-----------------------------------------#

class add_trainer_skill_map(generics.CreateAPIView):
    queryset = trainer_skill_map.objects.all()
    serializer_class = trainerSkillMapSerializer


@api_view(['GET'])
def get_trainer_skill_map(request):
    mapping = trainer_skill_map.objects.select_related('trainer_id', 'skill_id').all()

    map_data=[]
    for maps in  mapping:
           map_data.append({
              'id': maps.id,
              'trainer_id': maps.trainer_id.trainer_name,
              'skill_id': maps.skill_id.skill_name,
              'skill_level': maps.skill_level,
              'dt_skill_from': maps.dt_skill_from,
              'is_handson': maps.is_handson,
              'last_session': maps.last_session
            })
    return Response(map_data)

class update_trainer_skill_map(generics.UpdateAPIView):
    queryset = trainer_skill_map.objects.all()
    serializer_class = trainerSkillMapSerializer



@api_view(['PUT', 'PATCH'])
def delete_trainer_skill_map(request, pk):
    try:
        print("Entering Function..")
        skill_map = trainer_skill_map.objects.get(id=pk)

        print("skill_map: ", skill_map)
    except trainer_skill_map.DoesNotExist:
        return JsonResponse("skill_map not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    skill_map.deleted = 1
    skill_map.save()
    print("skill_map: ", skill_map)

    return JsonResponse("skill_map 'deleted' field updated successfully", safe=False)


#-----------------------------Trainer Skill Availability-----------------------------------------#

class add_trainer_availability(generics.CreateAPIView):
    queryset = trainer_availability.objects.all()
    serializer_class = trainerAvailabilitySerializer


@api_view(['GET'])
def get_trainer_availability(request):
    available = trainer_availability.objects.select_related('trainer_id', 'college_id', 'skill_id').all()

    available_data=[]
    for data in available:
        available_data.append({
            'id': data.id,
            'trainer_id': data.trainer_id.trainer_name,
            'is_available': data.is_available,
            'dtm_start': data.dtm_start,
            'dtm_stop': data.dtm_stop,
            'college_id': data.college_id.college_name,
            'skill_id': data.skill_id.skill_name
        })
    return Response(available_data)

class update_trainer_availability(generics.UpdateAPIView):
    queryset = trainer_availability.objects.all()
    serializer_class = trainerAvailabilitySerializer



@api_view(['PUT', 'PATCH'])
def delete_trainer_availability(request, pk):
    try:
        print("Entering Function..")
        available = trainer_availability.objects.get(id=pk)

        print("available: ", available)
    except trainer_availability.DoesNotExist:
        return JsonResponse("available not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    available.deleted = 1
    available.save()
    print("available: ", available)

    return JsonResponse("available 'deleted' field updated successfully", safe=False)



#-----------------------------Test Question Map-----------------------------------------#

class add_testQuestion_map(generics.CreateAPIView):
    queryset = test_question_map.objects.all()
    serializer_class = testQuestionMapSerializer


@api_view(['GET'])
def get_testQuestion_map(request):
    mapping = test_question_map.objects.select_related('test_id', 'question_id').all()

    mapping_data=[]
    for data in mapping:
        mapping_data.append({
            'id': data.id,
            'test_id': data.test_id.test_name,
            'question_id': data.question_id.question_name
        })
    return Response(mapping_data)

class update_testQuestion_map(generics.UpdateAPIView):
    queryset = test_question_map.objects.all()
    serializer_class = testQuestionMapSerializer



@api_view(['PUT', 'PATCH'])
def delete_testQuestion_map(request, pk):
    try:
        print("Entering Function..")
        mapping = test_question_map.objects.get(id=pk)

        print("mapping: ", mapping)
    except test_question_map.DoesNotExist:
        return JsonResponse("mapping not found", status=404)

    # Update the 'deleted' field to 1 instead of deleting the object
    mapping.deleted = 1
    mapping.save()
    print("mapping: ", mapping)

    return JsonResponse("mapping 'deleted' field updated successfully", safe=False)





#--------------------------------------Import Questions-----------------------------------#


class ExcelImportView_Questions(APIView):
    def post(self, request, format=None):
        print('Files:', request.FILES)
        
        if 'file' not in request.FILES:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        
        file = request.FILES['file']
        
        if not file.name.endswith('.xlsx'):
            return Response({'error': 'File is not in Excel format'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            df = pd.read_excel(file)
            print('DataFrame contents:')
            print(df.head())  # Print the first few rows of the DataFrame
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        # Replace question_type and skill_type values with their corresponding foreign key IDs
        for index, row in df.iterrows():
            question_type_name = row['question_type']
            skill_type_name = row['skill_type']
            question_type_id = question_type.objects.filter(question_type=question_type_name).first().id
            skill_type_id = skill_type.objects.filter(skill_type=skill_type_name).first().id
            df.at[index, 'question_type'] = question_type_id
            df.at[index, 'skill_type'] = skill_type_id
        
        records = df.to_dict(orient='records')
        
        serializer = questionsSerializerImport(data=records, many=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ExcelImportView_Tests(APIView):
    def post(self, request, format=None):
        print('Files:', request.FILES)
        
        if 'file' not in request.FILES:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        
        file = request.FILES['file']
        
        if not file.name.endswith('.xlsx'):
            return Response({'error': 'File is not in Excel format'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            df = pd.read_excel(file)
            print('DataFrame contents:')
            print(df.head())  # Print the first few rows of the DataFrame
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        # Replace question_type and skill_type values with their corresponding foreign key IDs
        for index, row in df.iterrows():
            test_type_name = row['test_type_id']
            question_type_name = row['question_type_id']
            course_name_id_name = row['course_id']
            college_name = row['college_id']
            department_name = row['department_id']
            
            id_test_type = test_type.objects.filter(test_type=test_type_name).first().id
            id_question_type = question_type.objects.filter(question_type=question_type_name).first().id
            id_course_name = courses_master.objects.filter(course_name=course_name_id_name).first().id
            id_college_name = college_master.objects.filter(college=college_name).first().id
            id_department_name = department_master.objects.filter(department=department_name).first().id

            df.at[index, 'test_type_id'] = id_test_type
            df.at[index, 'question_type_id'] = id_question_type
            df.at[index, 'course_id'] = id_course_name
            df.at[index, 'college_id'] = id_college_name
            df.at[index, 'department_id'] = id_department_name
        
        records = df.to_dict(orient='records')
        
        serializer = testsSerializersImport(data=records, many=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        




