#!/bin/bash

mongosh <<EOF
use map_my_world_db
db.createCollection("locations")
db.createCollection("categories")
db.createCollection("location_category_reviewed")
EOF