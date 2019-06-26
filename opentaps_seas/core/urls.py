# This file is part of opentaps Smart Energy Applications Suite (SEAS).

# opentaps Smart Energy Applications Suite (SEAS) is free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# opentaps Smart Energy Applications Suite (SEAS) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with opentaps Smart Energy Applications Suite (SEAS).
# If not, see <https://www.gnu.org/licenses/>.

from django.urls import path

from .views import (
    tag_list_view,
    tag_list_json_view,
    tag_detail_view,
    tag_edit_view,
    tag_create_view,
    tag_delete_view,
    model_list_view,
    model_list_json_view,
    model_detail_view,
    model_edit_view,
    model_create_view,
    model_delete_view,
    site_list_view,
    site_list_json_view,
    site_detail_view,
    site_create_view,
    state_list_json_view,
    timezone_list_json_view,
    site_pie_chart_data_json,
    site_ahu_summary_json,
    equipment_list_view,
    equipment_list_json_view,
    equipment_detail_view,
    equipment_site_detail_view,
    equipment_data_points_table,
    equipment_point_detail_view,
    equipment_create_view,
    point_detail_view,
    point_data_csv,
    point_data_json,
    entity_list_view,
    entity_detail_view,
    entity_file_upload,
    entity_tag,
    entity_note,
    entity_link,
    topic_list_view,
    topic_list_table,
    topic_setup_view,
    topic_assoc,
    topic_import_view,
    topic_rules,
    tag_topics
)

app_name = "core"
urlpatterns = [
    path("topic/", view=topic_list_view, name="topic_list"),
    path("tag_topics/", view=tag_topics, name="tag_topics"),
    path("topic_table/", view=topic_list_table, name="topic_table"),
    path("topic_rules/", view=topic_rules, name="topic_rules"),
    path("topic/import", view=topic_import_view, name="topic_import"),
    path("topic/setup/<path:topic>", view=topic_setup_view, name="topic_setup"),
    path("topic/assoc/<path:topic>", view=topic_assoc, name="topic_assoc"),
    path("entity/", view=entity_list_view, name="entity_list"),
    path("entity/<path:entity_id>", view=entity_detail_view, name="entity_detail"),
    path("file/entity/<path:entity_id>", view=entity_file_upload, name="entity_file_upload"),
    path("link/entity/<path:entity_id>", view=entity_link, name="entity_link"),
    path("note/entity/<path:entity_id>", view=entity_note, name="entity_note"),
    path("tag/entity/<path:entity_id>", view=entity_tag, name="entity_tag"),
    path("tag/", view=tag_list_view, name="tag_list"),
    path("tag.json", view=tag_list_json_view, name="tag_list_json"),
    path("newtag/", view=tag_create_view, name="tag_create"),
    path("tag/edit/<path:tag>", view=tag_edit_view, name="tag_edit"),
    path("tag/delete/<path:tag>", view=tag_delete_view, name="tag_delete"),
    path("tag/view/<path:tag>", view=tag_detail_view, name="tag_detail"),
    path("model/", view=model_list_view, name="model_list"),
    path("model.json", view=model_list_json_view, name="model_list_json"),
    path("newmodel/", view=model_create_view, name="model_create"),
    path("newsite/", view=site_create_view, name="site_create"),
    path("model/edit/<path:entity_id>", view=model_edit_view, name="model_edit"),
    path("model/delete/<path:entity_id>", view=model_delete_view, name="model_delete"),
    path("model/view/<path:entity_id>", view=model_detail_view, name="model_detail"),
    path("equipment.json", view=equipment_list_json_view, name="equipment_list_json"),
    path("equipment/", view=equipment_list_view, name="equipment_list"),
    path("equipment/<path:equip>", view=equipment_detail_view, name="equipment_detail"),
    path("equipment_points_table/<path:equip>", view=equipment_data_points_table, name="equipment_data_points_table"),
    path("site/<str:site>/newequipment/", view=equipment_create_view, name="equipment_create"),
    path("", view=site_list_view, name="site_list_default"),
    path("site/", view=site_list_view, name="site_list"),
    path("site.json", view=site_list_json_view, name="site_list_json"),
    path("site/<str:site>/", view=site_detail_view, name="site_detail"),
    path("site/<str:site>/pie_chart.json", view=site_pie_chart_data_json, name="site_pie_chart_data_json"),
    path("site/<str:site>/ahu_summary.json", view=site_ahu_summary_json, name="site_ahu_summary_json"),
    path("site/<str:site>/equipment/<str:equip>/", view=equipment_site_detail_view, name="site_equipment_detail"),
    path("site/<str:site>/equipment/<str:equip>/csv/<path:point>",
         view=point_data_csv, name="site_equipment_point_data_csv"),
    path("site/<str:site>/equipment/<str:equip>/json/<path:point>",
         view=point_data_json, name="site_equipment_point_data_json"),
    path("site/<str:site>/equipment/<str:equip>/<path:point>",
         view=equipment_point_detail_view, name="site_equipment_point_detail"),
    path("point/csv/<path:point>", view=point_data_csv, name="point_data_csv"),
    path("point/json/<path:point>", view=point_data_json, name="point_data_json"),
    path("point/<path:entity_id>", view=point_detail_view, name="point_detail"),
    path("state.json/<str:country>", view=state_list_json_view, name="state_list_json"),
    path("timezone.json/<str:geo_id>", view=timezone_list_json_view, name="timezone_list_json"),
]
