import datetime
from datetime import timedelta
from itertools import cycle

from django.contrib.auth.models import User, Group, Permission

from api.models import OrgGroup, Site
from people.models import Engineer, EngineerOrgGroupParticipation, SiteHoliday, Leave


# Create your tests here.
def create():
    # engineer_group = Group.objects.create(name="Engineers")
    manager_group = Group.objects.create(name="Manager")
    manager_group.permissions.set(Permission.objects.all())

    root_leader = User.objects.create_user(username="root_leader", password="password", is_staff=True)
    root_leader.groups.set([manager_group])
    root_member = User.objects.create_user(username="root_member", password="password", is_staff=True)
    root_member.groups.set([manager_group])
    root_guest = User.objects.create_user(username="root_guest", password="password", is_staff=True)
    root_guest.groups.set([manager_group])
    root_consumer = User.objects.create_user(username="root_consumer", password="password", is_staff=True)
    root_consumer.groups.set([manager_group])

    root_org = OrgGroup.objects.create(name="root_org", )
    # leaders = [root_leader], members = [root_member], guests = [root_guest], consumers = [root_consumer]
    root_org.leaders.set([root_leader])
    root_org.members.set([root_member])
    root_org.guests.set([root_guest])
    root_org.consumers.set([root_consumer])
    # root_org = OrgGroup.objects.save(root_org)

    l1_org1 = OrgGroup.objects.create(name="l1_org1", org_group=root_org)
    l1_org2 = OrgGroup.objects.create(name="l1_org2", org_group=root_org)

    l2_org11 = OrgGroup.objects.create(name="l2_org11", org_group=l1_org1)
    l2_org12 = OrgGroup.objects.create(name="l2_org12", org_group=l1_org1)
    l2_org21 = OrgGroup.objects.create(name="l2_org21", org_group=l1_org2)
    l2_org22 = OrgGroup.objects.create(name="l2_org22", org_group=l1_org2)

    l3_org111 = OrgGroup.objects.create(name="l3_org111", org_group=l2_org11)
    l3_org112 = OrgGroup.objects.create(name="l3_org112", org_group=l2_org11)
    l3_org121 = OrgGroup.objects.create(name="l3_org121", org_group=l2_org12)
    l3_org122 = OrgGroup.objects.create(name="l3_org122", org_group=l2_org12)
    l3_org211 = OrgGroup.objects.create(name="l3_org211", org_group=l2_org21)
    l3_org212 = OrgGroup.objects.create(name="l3_org212", org_group=l2_org21)
    l3_org221 = OrgGroup.objects.create(name="l3_org221", org_group=l2_org22)
    l3_org222 = OrgGroup.objects.create(name="l3_org222", org_group=l2_org22)

    org1_leader = User.objects.create_user(username="org1_leader", password="password", is_staff=True)
    org1_leader.groups.set([manager_group])
    l1_org1.leaders.set([org1_leader])

    org_groups = [l3_org111, l3_org112, l3_org121, l3_org122, l3_org211, l3_org212, l3_org221, l3_org222]

    org_site_1 = Site.objects.create(name='ODC1', summary='Offshore Dev Center 1')
    org_site_2 = Site.objects.create(name='ODC2', summary='Offshore Dev Center 1')

    site_holiday_1 = SiteHoliday.objects.create(site=org_site_1, name="org_site_1_holiday",
                                                date=datetime.date.today())
    site_holiday_2 = SiteHoliday.objects.create(site=org_site_2, name="org_site_2_holiday",
                                                date=datetime.date.today() + timedelta(days=1))

    org_sites = [org_site_1, org_site_2]
    org_sites_cycle = cycle(org_sites)

    eng_index = 0
    for org_group in org_groups:
        org_eng_user = User.objects.create_user(username=org_group.name + '_eng', password="password",
                                                is_staff=True)
        org_eng_user.groups.set([manager_group])

        org_eng = Engineer.objects.create(employee_id=org_group.name + '_eng_id', name=org_group.name + '_eng',
                                          auth_user=org_eng_user, role='engineer', site=next(org_sites_cycle))
        org_eng_participation = EngineerOrgGroupParticipation.objects.create(engineer=org_eng, role='engineer',
                                                                             capacity=1.0)
        org_eng_leave = Leave.objects.create(engineer=org_eng,
                                             start_date=datetime.date.today() + timedelta(days=(2 + eng_index)),
                                             end_date=datetime.date.today() + timedelta(days=(4 + eng_index)))
        eng_index += 1
