from flask import Flask, render_template, make_response, url_for, request
from flask_bootstrap import Bootstrap
from tempfile import mkdtemp
import uuid
import os
import csv
import randomname

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def render():
  return render_template('index.html')
  
@app.route('/download', methods=['POST'])
def download():
    # Generate n codes
    num_codes = int(request.form['num_codes'])
    prefix = request.form['name']
    
    uuids = [uuid.uuid4() for _ in range(int(num_codes))]
    
    # Create the CSVs
    temp_dir = mkdtemp()
    filename = prefix + '-' + str(num_codes) + '.csv'
    csv_codes = os.path.join(temp_dir, filename)
    with open(csv_codes, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['qr_code', 'link'])
        for id in uuids:
            writer.writerow([str(id), 'https://racquetpass.com/your-racquet/' + str(id)])
    
    # Return the CSV
    response = make_response(open(csv_codes, 'r').read())
    response.headers['Content-Disposition'] = 'attachment; filename={}, file2.csv'.format(filename)
    response.headers['Content-Type'] = 'text/csv'

    return response

if __name__ == '__main__':
  app.run(debug = True)

