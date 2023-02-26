from django.conf import settings
from django.conf.urls import include
from django.views.generic import RedirectView

from programme.views.paikkala_views import paikkala_special_reservation_view

from .views import (
    paikkala_inspection_view,
    paikkala_relinquish_view,
    paikkala_reservation_view,
    accept_invitation_view,
    admin_change_host_role_view,
    admin_change_invitation_role_view,
    admin_reservation_status_view,
    admin_reservations_export_view,
    admin_cold_offers_view,
    admin_cold_offers_view,
    admin_create_view,
    admin_detail_view,
    admin_email_list_view,
    admin_feedback_view,
    admin_invitations_view,
    admin_organizers_view,
    admin_publish_view,
    admin_rooms_view,
    admin_schedule_update_view_view,
    admin_schedule_view,
    admin_special_view,
    admin_view,
    admin_mail_editor_view,
    admin_mail_view,
    feedback_view,
    internal_adobe_taggedtext_view,
    internal_schedule_view,
    json_view,
    mobile_schedule_view,
    offer_form_view,
    offer_view,
    plaintext_view,
    profile_detail_view,
    profile_feedback_view,
    profile_reservations_view,
    profile_view,
    schedule_view,
    special_view,
)
from django.urls import re_path


app_name = "programme"
urlpatterns = [
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/timetable(?P<suffix>.*)",
        RedirectView.as_view(url="/events/%(event_slug)s/programme%(suffix)s", permanent=False),
        name="programme_old_urls_redirect",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/?$",
        schedule_view,
        dict(show_programme_actions=True),
        name="schedule_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/special/?$",
        special_view,
        dict(show_programme_actions=True),
        name="special_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/special/fragment/?$",
        special_view,
        dict(template="programme_list.pug"),
        name="special_fragment_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/fragment/?$",
        schedule_view,
        dict(template="programme_schedule_fragment.pug"),
        name="programme_schedule_fragment",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/mobile/?$",
        mobile_schedule_view,
        name="mobile_schedule_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/full/?$",
        internal_schedule_view,
        name="internal_schedule_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/new/?$",
        offer_view,
        name="offer_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/new/(?P<form_slug>[a-z0-9-]+)/?$",
        offer_form_view,
        name="offer_form_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/(?P<programme_id>\d+)/feedback/?$",
        feedback_view,
        name="feedback_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/(?P<programme_id>\d+)/reservations/(?P<pk>\d+)/relinquish/?$",
        paikkala_relinquish_view,
        name="paikkala_relinquish_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/(?P<programme_id>\d+)/reservations/(?P<pk>\d+)/inspect/(?P<key>.+?)/?$",
        paikkala_inspection_view,
        name="paikkala_inspection_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/(?P<programme_id>\d+)/reservations/?$",
        paikkala_reservation_view,
        name="paikkala_reservation_view",
    ),
    re_path(
        r"^reservations/(?P<code>[a-z0-9-]+)/?$",
        paikkala_special_reservation_view,
        name="paikkala_special_reservation_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme\.taggedtext$",
        internal_adobe_taggedtext_view,
        name="internal_adobe_taggedtext_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme\.txt$",
        plaintext_view,
        name="plaintext_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme\.json$",
        json_view,
        name="json_view_legacy_url",
    ),
    re_path(
        r"^api/v1/events/(?P<event_slug>[a-z0-9-]+)/programme$",
        json_view,
        name="json_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/desucon\.json$",
        json_view,
        dict(format="desucon"),
        name="moe_view",
    ),
    re_path(
        r"^api/v1/events/(?P<event_slug>[a-z0-9-]+)/programme/ropecon/?$",
        json_view,
        dict(format="ropecon"),
        name="rcon_view",
    ),
    re_path(
        r"^api/v1/events/(?P<event_slug>[a-z0-9-]+)/programme/hitpoint/?$",
        json_view,
        dict(format="hitpoint"),
        name="hitpoint_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/invitation/(?P<code>[a-f0-9]+)/?$",
        accept_invitation_view,
        name="accept_invitation_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/?$",
        admin_view,
        name="admin_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/new/?$",
        admin_create_view,
        name="admin_create_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/(?P<programme_id>\d+)/?$",
        admin_detail_view,
        name="admin_detail_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/(?P<programme_id>\d+)/invitations/(?P<invitation_id>\d+)/?$",
        admin_change_invitation_role_view,
        name="admin_change_invitation_role_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/(?P<programme_id>\d+)/reservations\.xlsx$",
        admin_reservations_export_view,
        name="admin_reservations_export_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/(?P<programme_id>\d+)/hosts/(?P<programme_role_id>\d+)/?$",
        admin_change_host_role_view,
        name="admin_change_host_role_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/invitations/?$",
        admin_invitations_view,
        name="admin_invitations_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/feedback/?$",
        admin_feedback_view,
        name="admin_feedback_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/organizers/?$",
        admin_organizers_view,
        name="admin_organizers_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/organizers\.(?P<format>\w+)?$",
        admin_organizers_view,
        name="admin_export_organizers_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/rooms/?$",
        admin_rooms_view,
        name="admin_rooms_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/schedule/?$",
        admin_schedule_view,
        name="admin_schedule_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/schedule/view/(?P<view_id>\d+)/?$",
        admin_schedule_update_view_view,
        name="admin_schedule_update_view_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/special/?$",
        admin_special_view,
        name="admin_special_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/publish/?$",
        admin_publish_view,
        name="admin_publish_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/start/?$",
        admin_cold_offers_view,
        name="admin_cold_offers_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/reservations/?$",
        admin_reservation_status_view,
        name="admin_reservation_status_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/programme\.(?P<format>xlsx|csv|tsv|html)$",
        admin_view,
        name="admin_export_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/emails\.txt$",
        admin_email_list_view,
        name="admin_email_list_view",
    ),
    re_path(r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/mail/?$", admin_mail_view, name="admin_mail_view"),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/mail/new/?$",
        admin_mail_editor_view,
        name="admin_mail_new_view",
    ),
    re_path(
        r"^events/(?P<event_slug>[a-z0-9-]+)/programme/admin/mail/(?P<message_id>\d+)/?$",
        admin_mail_editor_view,
        name="admin_mail_editor_view",
    ),
    re_path(
        r"^profile/programmes/?$",
        profile_view,
        name="profile_view",
    ),
    re_path(
        r"^profile/programmes/(?P<programme_id>\d+)/?$",
        profile_detail_view,
        name="profile_detail_view",
    ),
    re_path(
        r"^profile/programmes/(?P<programme_id>\d+)/feedback/?$",
        profile_feedback_view,
        name="profile_feedback_view",
    ),
    re_path(
        r"^profile/reservations/?",
        profile_reservations_view,
        name="profile_reservations_view",
    ),
]
