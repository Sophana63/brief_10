# ajout de send_form_directory pour les images
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, Flask
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

# ajout de ces modules pour les images
import os
from werkzeug.utils import secure_filename

bp = Blueprint('blog', __name__)
app = Flask(__name__)
@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/gears')
def gearindex():
    db = get_db()
    gears = db.execute(
        'SELECT id, name, desc, img'
        ' FROM gear'
        ' ORDER BY id ASC'
    ).fetchall()
    args = db.execute(
        'SELECT a.id AS id, type, content, g.id AS gid'
        ' FROM argument a JOIN gear_arg j ON j.id_arg = a.id'
        ' JOIN gear g ON j.id_gear = g.id'
        ' ORDER BY type ASC'
    ).fetchall()
    return render_template('gears/index.html', gears=gears, args=args)

@bp.route('/gears/create', methods=('GET', 'POST'))
@login_required
def gearcreate():
    db = get_db()
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']
        args = request.form.getlist('arg')
        # lié au fichier file
        UPLOAD_FOLDER = 'C:\\Users\\utilisateur\\brief_11_gears_museum\\brief_10\\flaskr\\static\\images'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        ALLOWED_EXTENSIONS = set(['img','jpg', 'jpeg', 'png'])

        def allowed_file(filename):
            return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        error = None

        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # path = os.path.join(app.root_path,'/images',img.filename)

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db.execute(
                'INSERT INTO gear (name, desc, img)'
                ' VALUES (?, ?, ?)',
                (name, desc, filename,)
            )
            db.commit()
            gid = db.execute(
                'SELECT id'
                ' FROM gear'
                ' ORDER BY id DESC'
                ' LIMIT 1'
            ).fetchone()
            for arg in args:
                db.execute(
                    'INSERT INTO gear_arg (id_gear, id_arg)'
                    ' VALUES (?, ?)',
                    (gid[0], arg,)
                )
                db.commit()
            return redirect(url_for('blog.gearindex'))
    argp = db.execute(
        'SELECT id, content'
        ' FROM argument'
        ' WHERE type = FALSE'
        ' ORDER BY id ASC'
    ).fetchall()
    argn = db.execute(
        'SELECT id, content'
        ' FROM argument'
        ' WHERE type = TRUE'
        ' ORDER BY id ASC'
    ).fetchall()
    return render_template('gears/create.html', argp=argp, argn=argn)


def get_gear(id):
    gear = get_db().execute(
        'SELECT id, name, desc, img'
        ' FROM gear'
        ' WHERE id = ?',
        (id,)
    ).fetchone()

    if gear is None:
        abort(404, f"Gear id {id} doesn't exist.")

    return gear


@bp.route('/gears/<int:id>/update', methods=('GET', 'POST'))
@login_required
def gearupdate(id):
    db = get_db()
    gear = get_gear(id)
    gearargs = db.execute(
        'SELECT id_arg'
        ' FROM gear_arg'
        ' WHERE id_gear = ?',
        (id,)
    ).fetchall()

    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']
        args = request.form.getlist('arg')
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db.execute(
                'UPDATE gear SET name = ?, desc = ?'
                ' WHERE id = ?',
                (name, desc, id,)
            )
            db.commit()
            db.execute(
                'DELETE FROM gear_arg'
                ' WHERE id_gear = ?',
                (id,)
            )
            for arg in args:
                db.execute(
                    'INSERT INTO gear_arg (id_gear, id_arg)'
                    ' VALUES (?, ?)',
                    (id, arg,)
                )
                db.commit()
            return redirect(url_for('blog.gearindex'))
    argp = db.execute(
        'SELECT id, content'
        ' FROM argument'
        ' WHERE type = FALSE'
        ' ORDER BY id ASC'
    ).fetchall()
    argn = db.execute(
        'SELECT id, content'
        ' FROM argument'
        ' WHERE type = TRUE'
        ' ORDER BY id ASC'
    ).fetchall()
    gargs = []
    for i in range (len(gearargs)):
        gargs.append(gearargs[i][0])
    return render_template('gears/update.html', gear=gear, gargs=gargs, argp=argp, argn=argn)


@bp.route('/gears/<int:id>/delete', methods=('POST',))
@login_required
def geardelete(id):
    get_gear(id)
    db = get_db()
    db.execute('DELETE FROM gear WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.gearindex'))


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))