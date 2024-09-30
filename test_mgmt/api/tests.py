from django.contrib.auth.models import User, Group, Permission
from django.test import TestCase

from api.models import OrgGroup
from api.serializers import UserSerializer, OrgGroupSerializer


# Create your tests here.

class BaseModelTestCase(TestCase):
    def setUp(self):
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

    def test_object_created(self):
        print("Running ", self)
        root_leader = User.objects.get(username="root_leader")
        root_member = User.objects.get(username="root_member")
        root_guest = User.objects.get(username="root_guest")
        root_consumer = User.objects.get(username="root_consumer")

        root_org = OrgGroup.objects.get(name="root_org")

        print(UserSerializer(root_leader).data)
        print(UserSerializer(root_member).data)
        print(UserSerializer(root_guest).data)
        print(UserSerializer(root_consumer).data)
        print(OrgGroupSerializer(root_org).data)

        print("Checking root_leader is leader ", root_org.is_owner(root_leader))
        print("Checking root_member is member ", root_org.is_member(root_member))
        print("Checking root_guest is guest ", root_org.is_guest(root_guest))
        print("Checking root_consumer is consumer ", root_org.is_consumer(root_consumer))

        print("Checking root_consumer is not leader ", not root_org.is_owner(root_consumer))
        print("Checking root_guest is not member ", not root_org.is_member(root_guest))
        print("Checking root_member is not guest ", not root_org.is_guest(root_member))
        print("Checking root_leader is not consumer ", not root_org.is_consumer(root_leader))

        print("Transitive sub orgs for root org ", root_org.get_transitive_sub_groups())
        print("Transitive sub orgs for l1_org1 ", OrgGroup.objects.get(name="l1_org1").get_transitive_sub_groups())
        print("Transitive sub orgs for l1_org2 ", OrgGroup.objects.get(name="l1_org2").get_transitive_sub_groups())
        print("Transitive sub orgs for l2_org11 ", OrgGroup.objects.get(name="l2_org11").get_transitive_sub_groups())
        print("Transitive sub orgs for l2_org12 ", OrgGroup.objects.get(name="l2_org12").get_transitive_sub_groups())
        print("Transitive sub orgs for l2_org21 ", OrgGroup.objects.get(name="l2_org21").get_transitive_sub_groups())
        print("Transitive sub orgs for l2_org22 ", OrgGroup.objects.get(name="l2_org22").get_transitive_sub_groups())

        print("Orgs for root_leader with delete is ", root_leader.get_orgs_with_delete_privileges())
        print("Orgs for root_member with delete is ", root_member.get_orgs_with_change_privileges())
        print("Orgs for root_guest with delete is ", root_guest.get_orgs_with_view_privileges())
        print("Orgs for root_consumer with delete is ", root_consumer.get_orgs_with_consumer_privileges())
        print("Orgs for root_leader with delete is ",
              User.objects.get(username="org1_leader").get_orgs_with_delete_privileges())
