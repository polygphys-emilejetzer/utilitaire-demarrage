#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import logging
import daemon
import schedule

from pathlib import Path

from polygphys.admin.heures import heures, exporter
# from polygphys.admin.inventaire import inventaire
from polygphys.admin.inventaire.importer import script as importer
from polygphys.admin.inventaire.zotero import script_zotero as zotero
from polygphys.sst.certificats_laser import nouveau_certificats, vérifier
from polygphys.sst.inscriptions_sst import inscriptions_sst
from polygphys.sst.trousses_premiers_soins import premiers_soins

# Configurer la journalisation


# Définir les fonctions de programmes


# Configurer l'horaire


# Fonction daemon


# Lancer le daemon

