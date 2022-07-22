import azure.functions as func
import logging
import os
from datetime import datetime
import psycopg2
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s', notification_id)
 
    # Done: Get connection to database
    connection = psycopg2.connect(host="mooc3-ptg-sv.postgres.database.azure.com",user="sa@mooc3-ptg-sv3",dbname="techconfdb", password="Aa@12345678")
    cursor = connection.cursor()
    try:
        # TODO: Get notification message and subject from database using the notification_id
        notification_message_subject = cursor.execute("select message, subject from notification where id = {};".format(notification_id))

        # TODO: Get attendees email and name
        cursor.execute("select first_name, last_name, email from attendee;")
        # TODO: Loop through each attendee and send an email with a personalized subject
        attendee_list = cursor.fetchall()
        for attendee in attendee_list:
            Mail('{}, {}, {}'.format({'udacity@techconf.com'}, {attendee[2]}, {notification_message_subject}))

        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        notification_date = datetime.utcnow()
        notification_status = 'Notified to {} attendees'.format(len(attendee_list))
        update_query = cursor.execute("UPDATE notification SET status = '{}', completed_date = '{}' WHERE id = {};".format(notification_status, notification_date, notification_id))        

        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
        # Done: Close connection