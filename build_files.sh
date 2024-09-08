echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
mkdir -p staticfiles_build

# Move collected static files to the `staticfiles_build` folder
mv static/* staticfiles_build/
echo "BUILD END"
