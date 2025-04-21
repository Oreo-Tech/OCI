import io
import json
from fdk import response

def handler(ctx, data: io.BytesIO = None):
    try:
        if data is None:
            print("No data received")
            return response.Response(ctx, response_data=json.dumps({"error": "No data"}), status_code=400)
        
        queue_data = data.getvalue()
        if not queue_data:
            print("Empty data received")
            return response.Response(ctx, response_data=json.dumps({"error": "Empty data"}), status_code=400)
        
        print(f"Message from queue: {queue_data.decode('utf-8')}")
        
        return response.Response(ctx, response_data=json.dumps({"status": "success"}))
    
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {str(e)}")
        return response.Response(ctx, response_data=json.dumps({"error": "Invalid JSON"}), status_code=400)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return response.Response(ctx, response_data=json.dumps({"error": str(e)}), status_code=500)
