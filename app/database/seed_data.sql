INSERT INTO doctors (first_name, last_name) VALUES ('John', 'Doe');
INSERT INTO doctors (first_name, last_name) VALUES ('Jane', 'Doe');
INSERT INTO doctors (first_name, last_name) VALUES ('Emily', 'Smith');

INSERT INTO locations (address) VALUES ('123 Main St');
INSERT INTO locations (address) VALUES ('456 Elm St');
INSERT INTO locations (address) VALUES ('789 Oak St');

INSERT INTO doctor_locations (doctor_id, location_id) VALUES (1, 1);
INSERT INTO doctor_locations (doctor_id, location_id) VALUES (1, 2);
INSERT INTO doctor_locations (doctor_id, location_id) VALUES (2, 2);
INSERT INTO doctor_locations (doctor_id, location_id) VALUES (2, 3);
INSERT INTO doctor_locations (doctor_id, location_id) VALUES (3, 3);

INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (1, 'Monday', '09:00:00', '17:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (1, 'Wednesday', '09:00:00', '17:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (1, 'Tuesday', '09:00:00', '17:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (1, 'Thursday', '09:00:00', '17:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (2, 'Tuesday', '10:00:00', '18:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (2, 'Thursday', '10:00:00', '18:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (2, 'Wednesday', '10:00:00', '18:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (2, 'Friday', '10:00:00', '18:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (3, 'Monday', '11:00:00', '19:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (3, 'Tuesday', '11:00:00', '19:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (3, 'Wednesday', '11:00:00', '19:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (3, 'Thursday', '11:00:00', '19:00:00');
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (3, 'Friday', '11:00:00', '19:00:00');


INSERT INTO appointments (doctor_id, location_id, appointment_time, duration) VALUES (1, 1, '2023-10-10 09:30:00', 30);
INSERT INTO appointments (doctor_id, location_id, appointment_time, duration) VALUES (1, 1, '2023-10-10 10:30:00', 30);
INSERT INTO appointments (doctor_id, location_id, appointment_time, duration) VALUES (2, 2, '2023-10-11 11:00:00', 30);
INSERT INTO appointments (doctor_id, location_id, appointment_time, duration) VALUES (2, 3, '2023-10-11 15:00:00', 30);
INSERT INTO appointments (doctor_id, location_id, appointment_time, duration) VALUES (3, 3, '2023-10-12 12:00:00', 30);
