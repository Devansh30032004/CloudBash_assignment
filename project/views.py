import requests
from django.shortcuts import render

def control_panel(request):
    # Default API content
    api_endpoint = None
    data = None

    if request.method == "POST":
        selected_api = request.POST.get("api_choice")
        
        if selected_api == "myntra":
            api_endpoint = "https://www.myntra.com/api/recommendations-endpoint-1"  # Replace with actual API
        elif selected_api == "meesho":
            api_endpoint = "https://www.meesho.com/api/recommendations-endpoint-2"  # Replace with actual API
        
        # Fetch data from the selected API
        if api_endpoint:
            try:
                response = requests.get(api_endpoint)
                if response.status_code == 200:
                    data = response.json()  # Parse API response
            except requests.exceptions.RequestException as e:
                data = {"error": str(e)}

    return render(request, "project/control_panel.html", {"data": data})
