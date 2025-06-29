import pandas as pd
import joblib
from django.shortcuts import render
from .forms import UploadCSVForm

# Load the trained ML model
model = joblib.load('model.pkl')

def upload_file(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)

            if all(col in df.columns for col in ['recency', 'frequency', 'monetary']):
                X = df[['recency', 'frequency', 'monetary']]
                df['prediction'] = model.predict(X)

                # ✅ Correct placement — inside the "if" block
                counts = df['prediction'].value_counts().to_dict()
                buy_count = counts.get(1, 0)
                no_buy_count = counts.get(0, 0)

                return render(request, 'result.html', {
                    'tables': df.to_html(),
                    'buy_count': buy_count,
                    'no_buy_count': no_buy_count
                })

            else:
                return render(request, 'upload.html', {
                    'form': form,
                    'error': 'CSV must have recency, frequency, and monetary columns.'
                })
    else:
        form = UploadCSVForm()

    return render(request, 'upload.html', {'form': form})
