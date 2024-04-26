from django.db import models

class appinfo(models.Model):
    info_code= models.CharField(max_length=50,null=True, blank=True)
    info_value= models.CharField(max_length=255,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class test_master(models.Model):
    test_name= models.CharField(max_length=255,null=True, blank=True)
    test_type_id=models.ForeignKey('test_type',on_delete=models.CASCADE)
    temp1= models.TextField(max_length=1000,null=True, blank=True)
    question_type_id=models.ForeignKey('question_type',on_delete=models.CASCADE)
    students_count= models.IntegerField(null=True, blank=True)
    dtm_start= models.DateTimeField(null=True, blank=True)
    dtm_end= models.DateTimeField(null=True, blank=True)
    college_id=models.ForeignKey('college_master',on_delete=models.CASCADE)
    duration= models.IntegerField(null=True, blank=True)
    year= models.CharField(max_length=50,null=True, blank=True)
    department_id=models.ForeignKey('department_master',on_delete=models.CASCADE)
    rules= models.CharField(max_length=1000,null=True, blank=True)
    course_id=models.ForeignKey('courses_master',on_delete=models.CASCADE)
    need_candidate_info= models.BooleanField(default=False)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class candidate_master(models.Model):
    college_id=models.ForeignKey('college_master',on_delete=models.CASCADE)
    students_name= models.CharField(max_length=255,null=True, blank=True)
    registration_number= models.CharField(max_length=255,null=True, blank=True)
    gender= models.CharField(max_length=255,null=True, blank=True)
    email_id= models.EmailField(null=True, blank=True)
    mobile_number= models.CharField(max_length=255,null=True, blank=True)
    department_id=models.ForeignKey('department_master',on_delete=models.CASCADE)
    year= models.CharField(max_length=50,null=True, blank=True)
    cgpa= models.CharField(max_length=255,null=True, blank=True)
    marks_10th= models.CharField(max_length=255,null=True, blank=True)
    marks_12th= models.CharField(max_length=255,null=True, blank=True)
    marks_semester_wise= models.CharField(max_length=1000,null=True, blank=True)
    history_of_arrears= models.CharField(max_length=1000,null=True, blank=True)
    standing_arrears= models.IntegerField(null=True, blank=True)
    number_of_offers= models.IntegerField(null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class college_admin(models.Model):
    admin_name= models.CharField(max_length=255,null=True, blank=True)
    college_id=models.ForeignKey('college_master',on_delete=models.CASCADE)
    admin_email= models.EmailField(null=True, blank=True)
    admin_phone= models.CharField(max_length=255,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class question_master(models.Model):
    question_name= models.TextField(max_length=1000,null=True, blank=True)
    question_text= models.TextField(max_length=1000,null=True, blank=True)
    topic_id=models.ForeignKey('topic_master',on_delete=models.CASCADE,null=True, blank=True)
    option_a= models.TextField(max_length=1000,null=True, blank=True)
    option_b= models.TextField(max_length=1000,null=True, blank=True)
    option_c= models.TextField(max_length=1000,null=True, blank=True)
    option_d= models.TextField(max_length=1000,null=True, blank=True)
    option_e= models.TextField(max_length=1000,null=True, blank=True)
    option_f= models.TextField(max_length=1000,null=True, blank=True)
    question_type_id=models.ForeignKey('question_type',on_delete=models.CASCADE)
    answer= models.TextField(max_length=1000,null=True, blank=True)
    negative_mark= models.IntegerField(null=True, blank=True)
    skill_id=models.ForeignKey('skills_master',on_delete=models.CASCADE)
    mark= models.IntegerField(null=True, blank=True)
    view_hint= models.TextField(max_length=1000,null=True, blank=True)
    explain_answer= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class skills_master(models.Model):
    skill_name= models.CharField(max_length=255,null=True, blank=True)
    skill_type_id=models.ForeignKey('skill_type',on_delete=models.CASCADE)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class skill_type(models.Model):
    skill_type= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class login(models.Model):
    email= models.EmailField(null=True, blank=True)
    user_name= models.CharField(max_length=100,unique=True)
    password= models.CharField(max_length=100,null=True, blank=True)
    role= models.CharField(max_length=100,null=True, blank=True)
    college_id=models.ForeignKey('college_master',on_delete=models.CASCADE)
class test_type(models.Model):
    test_type= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class question_type(models.Model):
    question_type= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class courses_master(models.Model):
    course_name= models.TextField(max_length=1000,null=True, blank=True)
    skill_id=models.ForeignKey('skills_master',on_delete=models.CASCADE)
    dtm_start= models.DateTimeField(null=True, blank=True)
    dtm_end= models.DateTimeField(null=True, blank=True)
    topic_id=models.ForeignKey('topic_master',on_delete=models.CASCADE,null=True, blank=True)
    is_active= models.BooleanField(default=False)
    course_count= models.IntegerField(null=True, blank=True)
    total_enrollment= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class course_contents(models.Model):
    course_id=models.ForeignKey('courses_master',on_delete=models.CASCADE)
    content_id=models.ForeignKey('content_master',on_delete=models.CASCADE)
    topic_id=models.ForeignKey('topic_master',on_delete=models.CASCADE,null=True, blank=True)
   # sub_topic_id= models.ForeignKey('topic_master',on_delete=models.CASCADE)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class course_candidates_map(models.Model):
    course_id=models.ForeignKey('courses_master',on_delete=models.CASCADE)
    student_id=models.ForeignKey('candidate_master',on_delete=models.CASCADE)
    dt_enrolled= models.DateField(null=True, blank=True)
    dt_validity= models.DateField(null=True, blank=True)
    status= models.CharField(max_length=100,null=True, blank=True)
    college_id=models.ForeignKey('college_master',on_delete=models.CASCADE)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class content_master(models.Model):
    content_type= models.CharField(max_length=100,null=True, blank=True)
    content_url= models.TextField(max_length=1000,null=True, blank=True)
    actual_content= models.TextField(max_length=1000,null=True, blank=True)
    status= models.CharField(max_length=255,null=True, blank=True)
    added_by= models.TextField(max_length=1000,null=True, blank=True)
    topic_id=models.ForeignKey('topic_master',on_delete=models.CASCADE,null=True, blank=True)
   # sub_topic_id=models.ForeignKey('topic_master',on_delete=models.CASCADE)
    size= models.PositiveIntegerField(null=True, blank=True)
    guidelines= models.TextField(max_length=1000,null=True, blank=True)
    dtm_active_from= models.DateTimeField(null=True, blank=True)
    dtm_validity= models.DateTimeField(null=True, blank=True)
    feedback= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class content_detail(models.Model):
    content_id=models.ForeignKey('content_master',on_delete=models.CASCADE)
    actual_content= models.TextField(max_length=1000,null=True, blank=True)
    status= models.CharField(max_length=100,null=True, blank=True)
    content_url= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class college_master(models.Model):
    college= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class department_master(models.Model):
    department= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class topic_master(models.Model):
    topic= models.TextField(max_length=1000,null=True, blank=True)
    sub_topic= models.TextField(max_length=1000,null=True, blank=True)
    is_active= models.BooleanField(default=False)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class tests_candidates_map(models.Model):
    test_id=models.ForeignKey('test_master',on_delete=models.CASCADE)
    question_id=models.ForeignKey('question_master',on_delete=models.CASCADE)
    student_id=models.ForeignKey('candidate_master',on_delete=models.CASCADE)
    college_id=models.ForeignKey('college_master',on_delete=models.CASCADE)
    department_id=models.ForeignKey('department_master',on_delete=models.CASCADE)
    dtm_start= models.DateTimeField(null=True, blank=True)
    dtm_end= models.DateTimeField(null=True, blank=True)
    dtm_schedule1_start= models.DateTimeField(null=True, blank=True)
    dtm_schedule1_end= models.DateTimeField(null=True, blank=True)
    dtm_schedule2_start= models.DateTimeField(null=True, blank=True)
    dtm_schedule2_end= models.DateTimeField(null=True, blank=True)
    attempt_count= models.IntegerField(null=True, blank=True)
    is_actual_test= models.BooleanField(default=False)
    duration= models.IntegerField(null=True, blank=True)
    year= models.CharField(max_length=50,null=True, blank=True)
    rules= models.TextField(max_length=1000,null=True, blank=True)
    video_required= models.BooleanField(default=False)
    is_active= models.BooleanField(default=False)
    need_candidate_info= models.BooleanField(default=False)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
    status= models.CharField(max_length=50,default=False)
class tests_candidates_answers(models.Model):
    student_id=models.ForeignKey('candidate_master',on_delete=models.CASCADE)
    test_id=models.ForeignKey('test_master',on_delete=models.CASCADE)
    question_id= models.ForeignKey('question_master', on_delete=models.CASCADE, null=True, blank=True)
    answer= models.TextField(max_length=1000,null=True, blank=True)
    result= models.IntegerField(null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class course_schedule(models.Model):
    student_id=models.ForeignKey('candidate_master',on_delete=models.CASCADE)
    course_id=models.ForeignKey('courses_master',on_delete=models.CASCADE)
    trainer_id=models.ForeignKey('trainer_master',on_delete=models.CASCADE)
    dtm_start= models.DateTimeField(null=True, blank=True)
    dtm_end= models.DateTimeField(null=True, blank=True)
    course_mode= models.CharField(max_length=255,null=True, blank=True)
    status= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class trainer_master(models.Model):
    trainer_name= models.CharField(max_length=255,null=True, blank=True)
    address= models.TextField(max_length=1000,null=True, blank=True)
    city= models.TextField(max_length=1000,null=True, blank=True)
    country= models.CharField(max_length=255,null=True, blank=True)
    qualification= models.TextField(max_length=1000,null=True, blank=True)
    is_active= models.BooleanField(default=False)
    preferred_city= models.CharField(max_length=255,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class course_content_feedback(models.Model):
    course_id=models.ForeignKey('courses_master',on_delete=models.CASCADE)
    student_id=models.ForeignKey('candidate_master',on_delete=models.CASCADE)
    topic_id=models.ForeignKey('topic_master',on_delete=models.CASCADE,null=True, blank=True)
    dtm_session= models.DateTimeField(null=True, blank=True)
    trainer_id=models.ForeignKey('trainer_master',on_delete=models.CASCADE)
    feedback= models.TextField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class attendance_master(models.Model):
    student_id=models.ForeignKey('candidate_master',on_delete=models.CASCADE)
    course_id=models.ForeignKey('courses_master',on_delete=models.CASCADE)
    test_id=models.ForeignKey('test_master',on_delete=models.CASCADE)
    dtm_attendance= models.DateTimeField(null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class announcement_master(models.Model):
    college_id=models.ForeignKey('college_master',on_delete=models.CASCADE)
    trainer_id=models.ForeignKey('trainer_master',on_delete=models.CASCADE)
    dtm_start= models.DateTimeField(null=True, blank=True)
    dtm_end= models.DateTimeField(null=True, blank=True)
    content= models.TextField(max_length=1000,null=True, blank=True)
    is_active= models.BooleanField(default=False)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class trainer_skill_map(models.Model):
    trainer_id=models.ForeignKey('trainer_master',on_delete=models.CASCADE)
    skill_id=models.ForeignKey('skills_master',on_delete=models.CASCADE)
    skill_level= models.IntegerField(null=True, blank=True)
    dt_skill_from= models.DateField(null=True, blank=True)
    is_handson= models.BooleanField(default=False)
    last_session= models.CharField(max_length=1000,null=True, blank=True)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class trainer_availability(models.Model):
    trainer_id=models.ForeignKey('trainer_master',on_delete=models.CASCADE)
    is_available= models.BooleanField(null=True, blank=True)
    dtm_start= models.DateTimeField(null=True, blank=True)
    dtm_stop= models.DateTimeField(null=True, blank=True)
    college_id=models.ForeignKey('college_master',on_delete=models.CASCADE)
    skill_id=models.ForeignKey('skills_master',on_delete=models.CASCADE)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)
class test_question_map(models.Model):
    test_id=models.ForeignKey('test_master',on_delete=models.CASCADE)
    question_id=models.ForeignKey('question_master',on_delete=models.CASCADE)
    deleted= models.IntegerField(default=0, null=True, blank=True)
    created_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_created= models.DateTimeField(null=True, blank=True)
    modified_by= models.CharField(max_length=100,null=True, blank=True)
    dtm_modified= models.DateTimeField(null=True, blank=True)
    remarks= models.TextField(max_length=1000,null=True, blank=True)
    dev_remarks= models.TextField(max_length=1000,null=True, blank=True)