# Wiki Monkey - MediaWiki bot and editor-assistant user script
# Copyright (C) 2011 Dario Giovannetti <dev@dariogiovannetti.net>
#
# This file is part of Wiki Monkey.
#
# Wiki Monkey is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Wiki Monkey is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Wiki Monkey.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask
from flask_cors import CORS


def run(cliargs):
    app = Flask(__name__)
    CORS(app, origins=cliargs.origins or ['*'])

    from . import models
    models.init(app, cliargs.db_path)
    # NOTE: It is necessary to *first* init the models and *then* the API
    from . import api
    api.init(app)

    app.run(host=cliargs.host,
            port=cliargs.port,
            ssl_context=(cliargs.ssl_cert, cliargs.ssl_key)
            if cliargs.ssl_cert and cliargs.ssl_key else 'adhoc',
            debug=cliargs.debug)
