from django.urls import path
from . import views
from .views import ExcelImportView_Questions, ExcelImportView_Tests

urlpatterns = [

    path('api/appinfo/', views.appinfogetAPIView.as_view(), name='appinfo-list'),
    path('api/appinfo/create/', views.appinfoAPIView.as_view(), name='appinfo-create'),
    path('api/appinfo/<int:pk>/', views.appinfoRetrieveUpdateDestroyAPIView.as_view(), name='appinfo-detail'),
   
    path('get/login/', views.get_login, name='login-retrive'),
    path('add/login/', views.login_create.as_view(), name='login-create'),
    path('update/login/<int:pk>/', views.update_login.as_view(), name='login-update'),
    path('delete/login/<int:pk>/', views.delete_login, name='login-delete'),
    
    path('api/skilltypes/', views.skilltypegetAPIView.as_view(), name='skilltype-list'),
    path('api/skilltypes/create/', views.skilltypecreateAPIView.as_view(), name='skilltype-create'),
    path('api/skilltypes/<int:pk>/', views.skilltypeRetrieveUpdateDestroyAPIView.as_view(), name='skilltype-detail'),
    path('api/skilltypes/<int:pk>/delete/', views.delete_skill_type, name='delete-skilltype'),

    path('api/testtypes/', views.test_type_listView.as_view(), name='testtypes-list'),
    path('api/testtypes/create/', views.test_type_create.as_view(), name='testtypes-create'),
    path('api/testtypes/<int:pk>/', views.test_type_Update.as_view(), name='testtypes-detail'),
    path('api/testtypes/<int:pk>/delete/', views.delete_test_type, name='delete-testtypes'),

    path('api/questiontypes/', views.question_type_listView.as_view(), name='questiontypes-list'),
    path('api/questiontypes/create/', views.question_type_create.as_view(), name='questiontypes-create'),
    path('api/questiontypes/<int:pk>/', views.question_type_Update.as_view(), name='questiontypes-detail'),
    path('api/questiontypes/<int:pk>/delete/', views.delete_question_type, name='delete-questiontypes'),

    path('colleges/', views.CollegeListView.as_view(), name='college-list'),
    path('colleges/create/', views.collegeCreateView.as_view(), name='college-create'),
    path('colleges/update/<int:pk>/', views.collegeUpdateView.as_view(), name='college-update'),
    path('colleges/delete/<int:pk>/', views.delete_college, name='college-delete'),

    # Department URLs
    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
    path('departments/create/', views.departmentCreateView.as_view(), name='department-create'),
    path('departments/update/<int:pk>/', views.departmentUpdateView.as_view(), name='department-update'),
    path('departments/delete/<int:pk>/', views.delete_department, name='department-delete'),
     
    path('api/topic/', views.topicListView.as_view(), name='topic-list'),
    path('api/topic/create/', views.topicCreateView.as_view(), name='topic-create'),
    path('api/topic/<int:pk>/', views.topicUpdateView.as_view(), name='topic-detail'),
    path('api/topic/<int:pk>/delete/', views.delete_topic, name='delete-topic'),

    path('api/skills/', views.get_skills, name='skill-list'),
    path('api/skills/create/', views.skillscreateAPIView.as_view(), name='skill-create'),
    path('api/skills/<int:pk>/', views.skillsRetrieveUpdateAPIView.as_view(), name='skill-detail'),
    path('api/skills/<int:pk>/delete/', views.delete_skills, name='delete-skill'),

    path('api/course/', views.get_course, name='course-list'),
    path('api/course/create/', views.coursecreateAPIView.as_view(), name='course-create'),
    path('api/course/<int:pk>/', views.courseUpdateAPIView.as_view(), name='course-detail'),
    path('api/course/<int:pk>/delete/', views.delete_course, name='delete-course'),
    
    path('api/candidates/', views.get_candidate, name='candidates-list'),
    path('api/candidates/create/', views.candidatescreateAPIView.as_view(), name='candidates-create'),
    path('api/candidates/<int:pk>/', views.candidates_Select_Update.as_view(), name='candidates-detail'),
    path('api/candidates/<int:pk>/delete/', views.delete_candidates, name='delete-candidates'),
    
    path('api/content/', views.get_content, name='content-list'),
    path('api/content/create/', views.contentcreateAPIView.as_view(), name='content-create'),
    path('api/content/<int:pk>/', views.contentUpdateAPIView.as_view(), name='content-detail'),
    path('api/content/<int:pk>/delete/', views.delete_content, name='delete-content'),

    path('api/trainers/', views.TrainerListAPIView.as_view(), name='trainer-list'),
    path('api/trainers/create/', views.TrainerCreateAPIView.as_view(), name='trainer-create'),
    path('api/trainers/<int:pk>/', views.TrainerRetrieveUpdateAPIView.as_view(), name='trainer-detail'),
    path('api/trainers/<int:pk>/delete/', views.delete_trainer, name='delete-trainer'),
   
    path('api/tests/get/', views.get_test, name='tests-list'),
   # path('api/tests/delete/<int:pk>/', views.testsRetrievedeleteAPIView.as_view(), name='tests-delete'),
    path('api/tests/create/', views.testcreateAPIView.as_view(), name='tests-create'),
    path('api/tests/<int:pk>/', views.testsRetrieveUpdateAPIView.as_view(), name='tests-detail'),
    path('api/tests/<int:pk>/delete/', views.delete_tests, name='delete-tests'),
   
    path('api/questions/', views.get_questions, name='questions-list'),
    path('api/questions/create/', views.questionscreateAPIView.as_view(), name='questions-create'),
    path('api/questions/<int:pk>/', views.questionsRetrieveUpdateAPIView.as_view(), name='questions-detail'),
    path('api/questions/<int:pk>/delete/', views.delete_question, name='delete-questions'),
  
    path('api/collegeadmin/', views.get_collegeadmin, name='admin-list'),
    path('api/collegeadmin/create/', views.collegeadmincreateAPIView.as_view(), name='admin-create'),
    path('api/collegeadmin/<int:pk>/', views.collegeadminRetrieveUpdateAPIView.as_view(), name='admin-detail'),
    path('api/collegeadmin/<int:pk>/delete/', views.delete_college_admin, name='delete-admmin'),
    
    path('course/content/', views.get_course_content, name='get_course_content'),
    path('course/content/create/', views.coursecontentscreateAPIView.as_view(), name='create_course_content'),
    path('course/content/update/<int:pk>/', views.coursecontentsUpdateAPIView.as_view(), name='update_course_content'),
    path('course/content/delete/<int:pk>/', views.delete_course_contents, name='delete_course_content'),
     
    path('api/course-candidates-map/', views.get_course_candidates_map, name='course-candidates-map'),
    path('api/course-candidates-map/create/', views.coursecandidatesmapcreateAPIView.as_view(), name='create-course-candidates-map'),
    path('api/course-candidates-map/update/<int:pk>/', views.coursecandidatesmapUpdateAPIView.as_view(), name='update-course-candidates-map'),
    path('api/course-candidates-map/delete/<int:pk>/', views.delete_course_can, name='delete-course-candidates-map'),

    path('api/content-detail/', views.get_content_detail, name='content-detail'),
    path('api/content-detail/create/', views.contentdetailcreateAPIView.as_view(), name='create-content-detail'),
    path('api/content-detail/update/<int:pk>/', views.coursecontentdetailUpdateAPIView.as_view(), name='update-content-detail'),
    path('api/content-detail/delete/<int:pk>/', views.delete_content_detail, name='delete-content-detail'),
   
    path('api/testcandidate/', views.get_tests_candidates_map, name='tests-candidates-map-list'),
    path('api/testcandidate/create/', views.testcandidatemapcreateAPIView.as_view(), name='tests-candidates-map-create'),
    path('api/testcandidate/<int:pk>/', views.testcandidatemapUpdateAPIView.as_view(), name='tests-candidates-map-detail'),
    path('api/testcandidate/<int:pk>/delete/', views.delete_testcandidatemap, name='delete-tests-candidates-map'),


    path('api/tests-candidates-answers/', views.get_tests_candidates_answer, name='tests-candidates-answers-list'),
    path('api/tests-candidates-answers/create/', views.testcandidateanscreateAPIView.as_view(), name='tests-candidates-answers-create'),
    path('api/tests-candidates-answers/<int:pk>/', views.testcandidateansUpdateAPIView.as_view(), name='tests-candidates-answers-detail'),
    path('api/tests-candidates-answers/<int:pk>/delete/', views.delete_testcandidatemap, name='delete-tests-candidates-answers'),
    

     path('get/course_contenet_feedback/', views.get_course_content_feedback, name='course_contenet_feedback-retrive'),
    path('add/course_contenet_feedback/', views.add_course_content_feedback.as_view(), name='course_contenet_feedback-create'),
    path('update/course_contenet_feedback/<int:pk>/', views.update_course_content_feedback.as_view(), name='course_contenet_feedback-update'),
    path('delete/course_contenet_feedback/<int:pk>/', views.delete_course_content_feedback, name='course_contenet_feedback-delete'),

    path('get/attendance_master/', views.get_attendance_master, name='attendance_master-retrive'),
    path('add/attendance_master/', views.add_attendance_master.as_view(), name='attendance_master-create'),
    path('update/attendance_master/<int:pk>/', views.update_attendance_master.as_view(), name='attendance_master-update'),
    path('delete/attendance_master/<int:pk>/', views.delete_attendance_master, name='delete_attendance_master-delete'),

    path('get/announcement_master/', views.get_announcement_master, name='announcement_master-retrive'),
    path('add/announcement_master/', views.add_announcement_master.as_view(), name='announcement_master-create'),
    path('update/announcement_master/<int:pk>/', views.update_announcement_master.as_view(), name='announcement_master-update'),
    path('delete/announcement_master/<int:pk>/', views.delete_announcement_master, name='announcement_master-delete'),

    path('get/trainer_skill_map/', views.get_trainer_skill_map, name='trainer_skill_map-retrive'),
    path('add/trainer_skill_map/', views.add_trainer_skill_map.as_view(), name='trainer_skill_map-create'),
    path('update/trainer_skill_map/<int:pk>/', views.update_trainer_skill_map.as_view(), name='trainer_skill_map-update'),
    path('delete/trainer_skill_map/<int:pk>/', views.delete_trainer_skill_map, name='announctrainer_skill_mapement_master-delete'),

    path('get/trainer_availability/', views.get_trainer_availability, name='trainer_availability-retrive'),
    path('add/trainer_availability/', views.add_trainer_availability.as_view(), name='trainer_availability-create'),
    path('update/trainer_availability/<int:pk>/', views.update_trainer_availability.as_view(), name='trainer_availability-update'),
    path('delete/trainer_availability/<int:pk>/', views.delete_trainer_availability, name='trainer_availability-delete'),

    path('get/test_question_map/', views.get_testQuestion_map, name='test_question_map-retrive'),
    path('add/test_question_map/', views.add_testQuestion_map.as_view(), name='test_question_map-create'),
    path('update/test_question_map/<int:pk>/', views.update_testQuestion_map.as_view(), name='test_question_map-update'),
    path('delete/test_question_map/<int:pk>/', views.delete_testQuestion_map, name='test_question_map-delete'),

    path('get/course_schedule/', views.get_course_schedule, name='course_schedule-retrive'),
    path('add/course_schedule/', views.add_course_schedule.as_view(), name='course_schedule-create'),
    path('update/course_schedule/<int:pk>/', views.update_course_schedule.as_view(), name='course_schedule-update'),
    path('delete/course_schedule/<int:pk>/', views.delete_course_schedule, name='course_schedule-delete'),
   
    path('question/import_excel/', ExcelImportView_Questions.as_view(), name='excel-import'),
    path('test/import_excel/', ExcelImportView_Tests.as_view(), name='excel-import-test'),
    
]