from rest_framework import serializers
from .models import appinfo,course_schedule,login,course_content_feedback, attendance_master, announcement_master, trainer_skill_map, trainer_availability, test_question_map,tests_candidates_map,tests_candidates_answers,content_detail,topic_master,course_contents,course_candidates_map,college_admin,question_master,skill_type,trainer_master,test_master,test_type,question_type,courses_master,candidate_master,skills_master,content_master,college_master,department_master

class appinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = appinfo
        fields = '__all__'
class testtypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = test_type
        fields = ['id', 'test_type']

class questiontypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = question_type
        fields = [ 'id', 'question_type']
class collegeSerializers(serializers.ModelSerializer):
    class Meta:
        model = college_master
        fields = [ 'id', 'college']

class departmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = department_master
        fields = [ 'id', 'department']
class topicSerializers(serializers.ModelSerializer):
    class Meta:
        model = topic_master
        fields = [ 'id', 'topic','sub_topic']
class skilltypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = skill_type
        fields = ['id','skill_type']

class skillSerializer(serializers.ModelSerializer):
    class Meta:
        model = skills_master
        fields = ['id','skill_name','skill_type_id']

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses_master
        fields = ['id','course_name','skill_id','topic_id','dtm_start','dtm_end','is_active','course_count','total_enrollment']


class candidatesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = candidate_master
        fields = ['id','college_id', 'students_name', 'registration_number', 'gender', 'email_id', 'mobile_number',
                  'department_id', 'year', 'cgpa', 'marks_10th', 'marks_12th', 'marks_semester_wise',
                  'history_of_arrears', 'standing_arrears', 'number_of_offers']
        
class contentSerializers(serializers.ModelSerializer):
    class Meta:
        model = content_master 
        fields =  ['id','content_type','content_url','actual_content','status','added_by','topic_id',
        'size','guidelines', 'dtm_active_from', 'dtm_validity', 'feedback']

class trainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = trainer_master
        fields = ['id','trainer_name','address','city','country','qualification','is_active','preferred_city']

class testsSerializers(serializers.ModelSerializer):
    class Meta:
        model = test_master
        fields = ['id','test_name', 'test_type_id','question_type_id','students_count', 'dtm_start','course_id',
        'dtm_end', 'college_id', 'duration', 'year', 'department_id', 'rules', 'need_candidate_info',]
class questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = question_master
        fields = [ 'id','question_name' ,'question_text','view_hint', 'option_a', 'option_b', 'option_c', 'option_d', 'option_e', 'option_f', 'question_type_id', 'skill_id','answer', 'negative_mark','mark','explain_answer','topic_id']
class collegeadminSerializers(serializers.ModelSerializer):
    class Meta:
        model = college_admin
        fields = ['id','admin_name', 'college_id']

    
class coursecontentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_contents
        fields = ['id','course_id', 'content_id', 'topic_id']

class coursecandidatesmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_candidates_map
        fields = ['id','course_id', 'student_id', 'dt_enrolled', 'dt_validity', 'status', 'college_id']

class contentdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = content_detail
        fields = ['id','content_id', 'actual_content', 'status', 'content_url']


class testcandidatemapSerializers(serializers.ModelSerializer):
    class Meta:
        model = tests_candidates_map
        fields = ['id','test_id','question_id','student_id','college_id', 'dtm_start',
        'dtm_end','dtm_schedule1_start','dtm_schedule1_end','dtm_schedule2_start','dtm_schedule2_end',
        'attempt_count','is_actual_test','department_id','duration','year','rules','is_active','need_candidate_info']

class tests_candidates_answerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tests_candidates_answers
        fields = ['id','student_id','question_id','answer','test_id','result']

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'
    
  
class courseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_schedule
        fields = ['student_id',
                  'course_id',
                  'trainer_id',
                  'dtm_start',
                  'dtm_end',
                  'course_mode',
                  'status']

  
class courseContentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_content_feedback
        fields = ['course_id',
                  'student_id',
                  'topic_id',
                  'dtm_session',
                  'trainer_id',
                  'feedback']
 
class attendanceMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance_master
        fields = ['student_id',
                  'course_id',
                  'test_id',
                  'dtm_attendance']


class announcementSerializer(serializers.ModelSerializer):
    class Meta:
        model = announcement_master
        fields = ['college_id',
                  'trainer_id',
                  'dtm_start',
                  'dtm_end',
                  'content',
                  'is_active']


class trainerSkillMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = trainer_skill_map
        fields = ['trainer_id',
                  'skill_id',
                  'skill_level',
                  'dt_skill_from',
                  'is_handson',
                  'last_session']


class trainerAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = trainer_availability
        fields = ['trainer_id',
                  'is_available',
                  'dtm_start',
                  'dtm_stop',
                  'college_id',
                  'skill_id']


class testQuestionMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = test_question_map
        fields = ['test_id',
                  'question_id']




#-------------------Import Serializers---------------------------------------#


class questionsSerializerImport(serializers.ModelSerializer):
    class Meta:
        model = question_master
        fields = [ 'question_name', 'question_text', 'topic_id', 'option_a', 'option_b', 'option_c', 'option_d', 'option_e', 'option_f', 'view_hint', 'mark', 'explain_answer', 'question_type_id',  'skill_id', 'answer', 'negative_mark']

    def create(self, validated_data):
        return question_master.objects.create(**validated_data)
    

class testsSerializersImport(serializers.ModelSerializer):
    class Meta:
        model = test_master
        fields = ['test_name', 'test_type_id','question_type_id','students_count', 'course_id', 'dtm_start', 'dtm_end', 'college_id', 'duration', 'year', 'rules', 'department_id', 'need_candidate_info']

    def create(self, validated_data):
        return test_master.objects.create(**validated_data)





