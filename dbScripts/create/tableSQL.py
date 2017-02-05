import MySQLdb
#Two dictionaries because create script hashes names and will create them out of order
TABLES = {}
TABLES2 = {}

TABLES['person'] = (
"CREATE TABLE IF NOT EXISTS person ("
" person_pk int(11) NOT NULL AUTO_INCREMENT,"
" name_last varchar(255) NOT NULL DEFAULT '',"
" name_first varchar(255) DEFAULT NULL,"
" name_index int(11) NOT NULL DEFAULT 0,"
" name_middle varchar(255) DEFAULT NULL,"
" name_spouse_or_partner_first varchar(255) DEFAULT NULL,"
" name_spouse_or_partner_last varchar(255) DEFAULT NULL,"
" name_legal_first varchar(255) DEFAULT NULL,"
" name_legal_middle varchar(255) DEFAULT NULL,"
" name_legal_last varchar(255) DEFAULT NULL,"
" prefix varchar(255) DEFAULT NULL,"
" suffix varchar(255) DEFAULT NULL,"
" salutation varchar(255) DEFAULT NULL,"
" home_street1 varchar(255) DEFAULT NULL,"
" home_street2 varchar(255) DEFAULT NULL,"
" home_city varchar(255) DEFAULT NULL,"
" home_state varchar(255) DEFAULT NULL,"
" home_zip varchar(255) DEFAULT NULL,"
" home_country varchar(255) DEFAULT NULL,"
" work_org varchar(255) DEFAULT NULL,"
" work_street1 varchar(255) DEFAULT NULL,"
" work_street2 varchar(255) DEFAULT NULL,"
" work_city varchar(255) DEFAULT NULL,"
" work_state varchar(255) DEFAULT NULL,"
" work_zip varchar(255) DEFAULT NULL,"
" work_country varchar(255) DEFAULT NULL,"
" phone_home varchar(255) DEFAULT NULL,"
" phone_work varchar(255) DEFAULT NULL,"
" phone_mobile varchar(255) DEFAULT NULL,"
" phone_fax varchar(255) DEFAULT NULL,"
" phone5 varchar(255) DEFAULT NULL,"
" phone6 varchar(255) DEFAULT NULL,"
" email varchar(255) DEFAULT NULL,"
" email2 varchar(255) DEFAULT NULL,"
" website varchar(255) DEFAULT NULL,"
" preferred_communication enum('home','work','mobile','email','mail','special') DEFAULT NULL,"
" preferred_communication_text varchar(255) DEFAULT NULL,"
" preferred_address enum('home','work') DEFAULT NULL,"
" use_housing tinyint(1) DEFAULT NULL,"
" smoker tinyint(1) DEFAULT NULL,"
" pet_allergies tinyint(1) DEFAULT NULL,"
" pets tinyint(1) DEFAULT NULL,"
" kids tinyint(1) DEFAULT NULL,"
" physical_considerations text,"
" dietary_needs text,"
" appellation varchar(255) DEFAULT NULL,"
" bio text,"
" photo varchar(255) DEFAULT NULL,"
" include_in_directory tinyint(1) DEFAULT NULL,"
" participant_notes text,"
" contact_notes text,"
" available_1A tinyint(1) DEFAULT NULL,"
" available_1P tinyint(1) DEFAULT NULL,"
" available_2A tinyint(1) DEFAULT NULL,"
" available_2P tinyint(1) DEFAULT NULL,"
" available_3A tinyint(1) DEFAULT NULL,"
" available_3P tinyint(1) DEFAULT NULL,"
" available_4A tinyint(1) DEFAULT NULL,"
" available_4P tinyint(1) DEFAULT NULL,"
" available_5A tinyint(1) DEFAULT NULL,"
" available_5P tinyint(1) DEFAULT NULL,"
" interest_x_dis tinyint(1) DEFAULT NULL,"
" interest_arts tinyint(1) DEFAULT NULL,"
" interest_bus tinyint(1) DEFAULT NULL,"
" interest_hc tinyint(1) DEFAULT NULL,"
" interest_ia tinyint(1) DEFAULT NULL,"
" interest_med tinyint(1) DEFAULT NULL,"
" interest_pol tinyint(1) DEFAULT NULL,"
" interest_st tinyint(1) DEFAULT NULL,"
" venue_manager tinyint(1) DEFAULT NULL,"
" committee_arts tinyint(1) DEFAULT NULL,"
" committee_bus tinyint(1) DEFAULT NULL,"
" committee_hc tinyint(1) DEFAULT NULL,"
" committee_ia tinyint(1) DEFAULT NULL,"
" committee_pol tinyint(1) DEFAULT NULL,"
" committee_st tinyint(1) DEFAULT NULL,"
" committee_students tinyint(1) DEFAULT NULL,"
" committee_housing tinyint(1) DEFAULT NULL,"
" committee_moderator tinyint(1) DEFAULT NULL,"
" committee_volunteer tinyint(1) DEFAULT NULL,"
" committee_fundraising tinyint(1) DEFAULT NULL,"
" committee_office tinyint(1) DEFAULT NULL,"
" committee_other tinyint(1) DEFAULT NULL,"
" committee_notes text,"
" houser_fk int(11) DEFAULT NULL,"
" housed_fk int(11) DEFAULT NULL,"
" contact_fk int(11) DEFAULT NULL,"
" hyphen_fk int(11) DEFAULT NULL,"
" introduced_by_fk int(11) DEFAULT NULL,"
" committee_contact_fk int(11) DEFAULT NULL,"
" donor tinyint(1) DEFAULT NULL,"
" houser tinyint(1) DEFAULT NULL,"
" moderator tinyint(1) DEFAULT NULL,"
" producer tinyint(1) DEFAULT NULL,"
" committee_member tinyint(1) DEFAULT NULL,"
" participant tinyint(1) DEFAULT NULL,"
" fan tinyint(1) DEFAULT NULL,"
" student tinyint(1) DEFAULT NULL,"
" volunteer tinyint(1) DEFAULT NULL,"
" staff tinyint(1) DEFAULT NULL,"
" companion tinyint(1) DEFAULT NULL,"
" id_number int(11) DEFAULT NULL,"
" deceased tinyint(1) DEFAULT NULL,"
" load_donation tinyint(1) DEFAULT NULL,"
" load_panel tinyint(1) DEFAULT NULL,"
" load_participant tinyint(1) DEFAULT NULL,"
" conversion_note text,"
" replacedby_fk int(11) DEFAULT NULL,"
" companion_to_fk int(11) DEFAULT NULL,"
" name_for_program varchar(255) DEFAULT NULL,"
" gender enum('male','female') DEFAULT NULL,"
" companion_type enum('spouse/partner','child','friend') DEFAULT NULL,"
" days_here varchar(20) DEFAULT NULL,"
" new_or_returning enum('new','returning') DEFAULT NULL,"
" confirmation_sheet tinyint(1) DEFAULT NULL,"
" bio_in tinyint(1) DEFAULT NULL,"
" photo_in tinyint(1) DEFAULT NULL,"
" birthday date DEFAULT NULL,"
" date_topics_letter_sent date DEFAULT NULL,"
" topics_received tinyint(1) DEFAULT NULL,"
" rating enum('A','B','C','D','F') DEFAULT NULL,"
" flight_info_received tinyint(1) DEFAULT NULL,"
" transportation_email_sent tinyint(1) DEFAULT NULL,"
" bringing_children tinyint(1) DEFAULT NULL,"
" date_address_verfied date DEFAULT NULL,"
" subcommittee enum('Arts','Bus','HC','IA','Pol','ST','Student','Floater','Jazz') DEFAULT NULL,"
" subcommittee2 enum('Arts','Bus','HC','IA','Pol','ST','Student','Floater','Jazz') DEFAULT NULL,"
" abbreviation varchar(5) DEFAULT NULL,"
" how_topics_letter_sent enum('letter','email','both') DEFAULT NULL,"
" include_in_directory_choice enum('yes','no','special') DEFAULT NULL,"
" housing_notes text,"
" panel_notes text,"
" is_organization tinyint(4) NOT NULL DEFAULT 0,"
" committee_member_former tinyint(1) DEFAULT NULL,"
" autoload tinyint(1) DEFAULT NULL,"
" notes_directory text,"
" notes_followup text,"
" same_addr_as_partner tinyint(1) DEFAULT NULL,"
" no_mail_solicit tinyint(1) NOT NULL DEFAULT 0,"
" bad_address tinyint(1) NOT NULL DEFAULT 0,"
" no_email_solicit tinyint(1) NOT NULL DEFAULT 0,"
" moderator_info text,"
" moderator_program_name varchar(255) DEFAULT NULL,"
" moderator_notes text,"
" moderator_interest_notes text,"
" moderator_availability_notes text,"
" moderator_tier varchar(255) DEFAULT NULL,"
" divorced tinyint(1) DEFAULT NULL,"
" divorced_note varchar(255) DEFAULT NULL,"
" board tinyint(1) DEFAULT NULL,"
" guest_speaker tinyint(1) DEFAULT NULL,"
" time_leaving time DEFAULT NULL,"
" candidate tinyint(1) DEFAULT NULL,"
" PRIMARY KEY (person_pk),"
" UNIQUE KEY person_name (name_last,name_first,name_index),"
" UNIQUE KEY person_abbreviation (abbreviation),"
" KEY constraint_person_houser_fk (houser_fk),"
" KEY constraint_person_housed_fk (housed_fk),"
" KEY constraint_person_hyphen_fk (hyphen_fk),"
" KEY constraint_person_introduced_by_fk (introduced_by_fk),"
" KEY constraint_person_committee_contact_fk (committee_contact_fk),"
" KEY constraint_person_contact_fk (contact_fk),"
" KEY constraint_person_replacedby_fk (replacedby_fk),"
" KEY constraint_person_companion_to_fk (companion_to_fk),"
" CONSTRAINT constraint_person_committee_contact_fk"
" FOREIGN KEY (committee_contact_fk)"
" REFERENCES person (person_pk)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION,"
" CONSTRAINT constraint_person_companion_to_fk"
" FOREIGN KEY (companion_to_fk)"
" REFERENCES person (person_pk)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION,"
" CONSTRAINT constraint_person_contact_fk"
" FOREIGN KEY (contact_fk)"
" REFERENCES person (person_pk)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION,"
" CONSTRAINT constraint_person_hyphen_fk"
" FOREIGN KEY (hyphen_fk)"
" REFERENCES person (person_pk)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION,"
" CONSTRAINT constraint_person_introduced_by_fk"
" FOREIGN KEY (introduced_by_fk)"
" REFERENCES person (person_pk)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION,"
" CONSTRAINT constraint_person_replacedby_fk"
" FOREIGN KEY (replacedby_fk)"
" REFERENCES person (person_pk)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION"
") ENGINE=InnoDB AUTO_INCREMENT=14793 DEFAULT CHARSET=utf8")

TABLES2['VMS_jobs'] = (
"CREATE TABLE IF NOT EXISTS VMS_jobs ("
" job_id int(11) NOT NULL,"
" assigned_number int(11) NOT NULL,"
" person_id int(11) NOT NULL,"
" filled tinyint(1) NOT NULL,"
" PRIMARY KEY (job_id,assigned_number),"
" CONSTRAINT job_id_job_assignments"
" FOREIGN KEY (job_id)"
" REFERENCES VMS_job_instances (job_id)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION,"
" CONSTRAINT person_id_job_assignments"
" FOREIGN KEY (person_id)"
" REFERENCES VMS_persons (person_id)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION"
") ENGINE=InnoDB DEFAULT CHARSET=utf8")

TABLES2['VMS_job_instances'] = (
"CREATE TABLE IF NOT EXISTS VMS_job_instances ("
" job_id int(11) NOT NULL AUTO_INCREMENT,"
" job_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP"
" ON UPDATE CURRENT_TIMESTAMP,"
" location varchar(30) NOT NULL,"
" job_type_id int(11) NOT NULL,"
" job_discription varchar(200) DEFAULT NULL,"
" volunteers_needed int(11) NOT NULL,"
" PRIMARY KEY (job_id),"
" KEY job_type_id_job_instances (job_type_id),"
" CONSTRAINT job_type_id_job_instances"
" FOREIGN KEY (job_type_id)"
" REFERENCES VMS_job_types (job_type_id)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION"
") ENGINE=InnoDB DEFAULT CHARSET=utf8")

TABLES2['VMS_job_skills'] = (
"CREATE TABLE IF NOT EXISTS VMS_job_skills ("
" job_type_id int(11) NOT NULL,"
" skill_number int(11) NOT NULL,"
" skill_id int(11) NOT NULL,"
" PRIMARY KEY (job_type_id,skill_number),"
" KEY skill_id_job_skills (skill_id),"
" CONSTRAINT job_type_id_job_skills"
" FOREIGN KEY (job_type_id)"
" REFERENCES VMS_job_types (job_type_id)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION,"
" CONSTRAINT skill_id_job_skills"
" FOREIGN KEY (skill_id)"
" REFERENCES VMS_skills (skill_id)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION"
") ENGINE=InnoDB DEFAULT CHARSET=utf8")

TABLES['VMS_job_types'] = (
"CREATE TABLE IF NOT EXISTS VMS_job_types ("
" job_type_id int(11) NOT NULL AUTO_INCREMENT,"
" job_type_name varchar(30) NOT NULL,"
" job_type_discription varchar(200) NOT NULL,"
" PRIMARY KEY (job_type_id)"
") ENGINE=InnoDB DEFAULT CHARSET=utf8")

TABLES2['VMS_message_details'] = (
"CREATE TABLE IF NOT EXISTS VMS_message_details ("
" message_id int(11) NOT NULL,"
" message_type_id int(11) NOT NULL,"
" content varchar(50) NOT NULL,"
" PRIMARY KEY (message_id),"
" KEY message_type_id_message_details (message_type_id),"
"CONSTRAINT message_type_id_message_details"
" FOREIGN KEY (message_type_id)"
" REFERENCES VMS_message_types (message_type_id)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION"
") ENGINE=InnoDB DEFAULT CHARSET=utf8")

TABLES['VMS_message_types'] = (
"CREATE TABLE IF NOT EXISTS VMS_message_types ("
" message_type_id int(11) NOT NULL,"
" message_type varchar(20) NOT NULL,"
" PRIMARY KEY (message_type_id)"
") ENGINE=InnoDB DEFAULT CHARSET=utf8")

TABLES['VMS_persons'] = (
"CREATE TABLE IF NOT EXISTS VMS_persons ("
" person_id int(11) NOT NULL AUTO_INCREMENT,"
" first_name varchar(30) NOT NULL,"
" last_name varchar(30) NOT NULL,"
" username varchar(30) NOT NULL,"
" email varchar(60) NOT NULL,"
" phone varchar(30) NOT NULL,"
" password varchar(60) NOT NULL,"
" admin_status tinyint(1) NOT NULL DEFAULT 0,"
" alum tinyint(1) NOT NULL DEFAULT 0,"
" graduation_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP"
" ON UPDATE CURRENT_TIMESTAMP,"
" PRIMARY KEY (person_id)"
") ENGINE=InnoDB DEFAULT CHARSET=utf8")

TABLES['VMS_skills'] = (
"CREATE TABLE IF NOT EXISTS VMS_skills ("
" skill_id int(11) NOT NULL AUTO_INCREMENT,"
" skill_name varchar(30) NOT NULL,"
" discription varchar(200) NOT NULL,"
" PRIMARY KEY (skill_id)"
") ENGINE=InnoDB DEFAULT CHARSET=utf8")

TABLES2['VMS_volunteer_available_time_nodes'] = (
"CREATE TABLE IF NOT EXISTS VMS_volunteer_available_time_nodes ("
" person_id int(11) NOT NULL,"
" time_seq int(11) NOT NULL,"
" time_node timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP"
" ON UPDATE CURRENT_TIMESTAMP,"
" PRIMARY KEY (person_id,time_seq),"
" CONSTRAINT person_id_volunteer_available_time_nodes"
" FOREIGN KEY (person_id)"
" REFERENCES VMS_persons (person_id)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION"
") ENGINE=InnoDB DEFAULT CHARSET=utf8")

TABLES2['VMS_volunteer_skills'] = (
"CREATE TABLE IF NOT EXISTS VMS_volunteer_skills ("
" person_id int(11) NOT NULL,"
" skill_number int(11) NOT NULL,"
" skill_id int(11) NOT NULL,"
" PRIMARY KEY (person_id,skill_number),"
" KEY skills_id_volunteer_skills (skill_id),"
" CONSTRAINT person_id_volunteer_skills"
" FOREIGN KEY (person_id)"
" REFERENCES VMS_persons (person_id)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION,"
" CONSTRAINT skills_id_volunteer_skills"
" FOREIGN KEY (skill_id)"
" REFERENCES VMS_skills (skill_id)"
" ON DELETE NO ACTION"
" ON UPDATE NO ACTION"
") ENGINE=InnoDB DEFAULT CHARSET=utf8")

