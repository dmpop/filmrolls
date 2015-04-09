#!/usr/bin/python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sqlite3, os
from bottle import route, redirect, run, debug, template, request, static_file

@route('/filmrolls')
def filmrolls():
    if os.path.exists('filmrolls.sqlite'):
        conn = sqlite3.connect('filmrolls.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM rolls ORDER BY dt DESC")
        result = c.fetchall()
        c.close()
        output = template('filmrolls.tpl', rows=result)
        return output
    else:
        conn = sqlite3.connect('filmrolls.sqlite')
        conn.execute("CREATE TABLE rolls (id INTEGER PRIMARY KEY  NOT NULL, order_no INTEGER DEFAULT (null), dt DATETIME DEFAULT (CURRENT_DATE), camera VARCHAR,film VARCHAR)")
        conn.commit()
        return redirect('/filmrolls')

@route('/add', method='GET')
def new_roll():
    if request.GET.get('add','').strip():
        order_no = request.GET.get('order_no', '').strip()
        dt = request.GET.get('dt', '').strip()
        camera = request.GET.get('camera', '').strip()
        film = request.GET.get('film', '').strip()
        conn = sqlite3.connect('filmrolls.sqlite')
        c = conn.cursor()

        c.execute("INSERT INTO rolls (order_no, dt, camera, film) VALUES (?,?,?,?)", (order_no,dt, camera,film))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return redirect('/filmrolls')
    else:
        return template('add_roll.tpl')

@route('/edit/:no', method='GET')
def edit_roll(no):

    if request.GET.get('save','').strip():
        order_no = request.GET.get('order_no', '').strip()
        dt = request.GET.get('dt', '').strip()
        camera = request.GET.get('camera', '').strip()
        film = request.GET.get('film', '').strip()
        conn = sqlite3.connect('filmrolls.sqlite')
        c = conn.cursor()
        c.execute("UPDATE rolls SET order_no = ?, dt = ?, camera = ?, film = ? WHERE id LIKE ?", (order_no, dt, camera, film, no))
        conn.commit()

        return redirect('/filmrolls')
    else:
        conn = sqlite3.connect('filmrolls.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM rolls WHERE id LIKE ?", (str(no), ))
        cur_data = c.fetchone()

        return template('edit_roll.tpl', old=cur_data, no=no)

@route('/delete/:no', method='GET')
def delete_roll(no):

    if request.GET.get('delete','').strip():
        conn = sqlite3.connect('filmrolls.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM rolls WHERE id LIKE ?", (no, ))
        conn.commit()

        return redirect('/filmrolls')
    else:
        return template('delete_roll.tpl', no=no)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host="0.0.0.0",port=8080, debug=True, reloader=True)
