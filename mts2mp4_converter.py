import subprocess

input_file = '/Users/phoenix/Downloads/DD_National-01022000-0014-P1.mts'
output_file = '/Users/phoenix/Downloads/DD_National-01022000-0014-P1.mp4'

command = [
    'ffmpeg',
    '-analyzeduration', '1000M',
    '-probesize', '1000M',
    '-i', input_file,
    '-vf', 'scale=1280:720',
    '-y',  # Overwrite output file if it already exists
    output_file
]

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

while True:
    output = process.stdout.readline()
    if process.poll() is not None:
        break
    if output:
        print(output.strip().decode())

if process.returncode == 0:
    print('Conversion completed successfully.')
else:
    print('An error occurred during conversion.')
