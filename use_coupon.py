import pymysql
import os

def lambda_handler(event, context):
    user_id = event['pathParameters']['id']

    connection = pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME'],
        connect_timeout=5
    )

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE users SET coupon = coupon - 1 WHERE id = %s AND coupon > 0"
            cursor.execute(sql, (user_id,))
        connection.commit()
        return {
            "statusCode": 200,
            "body": "쿠폰 지급 완료"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
    finally:
        connection.close()

