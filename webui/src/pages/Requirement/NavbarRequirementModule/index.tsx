import React, { useState } from "react";
import { createStyles, Navbar, Group, Code } from "@mantine/core";
import {
  IconHome,
  IconBook,
  IconUser,
  IconCalendar,
  IconTruckReturn,
  IconLogout,
} from "@tabler/icons";
import { useNavigate, useParams } from "react-router-dom";
import { authState } from "../../../state/authData";
import { useRecoilValue } from "recoil";
import { Form } from "react-bootstrap";
import { axiosClientBasic } from "../../../hooks/api";

const useStyles = createStyles((theme, _params, getRef) => {
  const icon = getRef("icon");
  return {
    navbar: {
      backgroundColor: theme.fn.variant({
        variant: "filled",
        // color: theme.primaryColor,
      }).background,
    },

    version: {
      backgroundColor: theme.fn.lighten(
        theme.fn.variant({ variant: "filled", color: theme.primaryColor })
          .background!,
        0.1
      ),
      color: theme.white,
      fontWeight: 700,
    },

    header: {
      paddingBottom: theme.spacing.md,
      marginBottom: theme.spacing.md * 1.5,
      borderBottom: `1px solid ${theme.fn.lighten(
        theme.fn.variant({ variant: "filled", color: theme.primaryColor })
          .background!,
        0.1
      )}`,
    },

    footer: {
      paddingTop: theme.spacing.md,
      marginTop: theme.spacing.md,
      borderTop: `1px solid ${theme.fn.lighten(
        theme.fn.variant({ variant: "filled", color: theme.primaryColor })
          .background!,
        0.1
      )}`,
    },

    link: {
      ...theme.fn.focusStyles(),
      display: "flex",
      alignItems: "center",
      textDecoration: "none",
      fontSize: theme.fontSizes.sm,
      color: theme.white,
      padding: `${theme.spacing.xs}px ${theme.spacing.sm}px`,
      borderRadius: theme.radius.sm,
      fontWeight: 500,

      "&:hover": {
        backgroundColor: theme.fn.lighten(
          theme.fn.variant({ variant: "filled", color: theme.primaryColor })
            .background!,
          0.1
        ),
      },
    },

    linkIcon: {
      ref: icon,
      color: theme.white,
      opacity: 0.75,
      marginRight: theme.spacing.sm,
    },

    linkActive: {
      "&, &:hover": {
        backgroundColor: theme.fn.lighten(
          theme.fn.variant({ variant: "filled", color: theme.primaryColor })
            .background!,
          0.15
        ),
        [`& .${icon}`]: {
          opacity: 0.9,
        },
      },
    },
  };
});

const data = [
  { link: "/requirements/default", label: "REQUIREMENTS", icon: IconHome },
  {
    link: "/requirements/use-cases",
    label: "USE CASES",
    icon: IconBook,
  },
  {
    link: "/requirements/another-item",
    label: "ANOTHER ITEM",
    icon: IconUser,
  },
  // { link: "/capacity-planner/leaves", label: "LEAVES", icon: IconCalendar },
  // { link: "", label: "Databases", icon: IconDatabaseImport },
  // { link: "", label: "Authentication", icon: Icon2fa },
  // { link: "", label: "Other Settings", icon: IconSettings },
];

export function NavbarRequirementModule() {
  const { orggroup } = useParams();
  const navigate = useNavigate();
  const { classes, cx } = useStyles();
  const [active, setActive] = useState("Billing");
  const auth = useRecoilValue(authState);
  const [orgGroups, setOrgGroups] = React.useState<any[]>([]);
  const [selectedOrgGrp, setSelectedOrgGrp] = React.useState("Default");

  const links = data.map((item) => (
    <a
      className={cx(classes.link, {
        [classes.linkActive]: item.label === active,
      })}
      href={item.link}
      key={item.label}
      onClick={(event) => {
        event.preventDefault();
        setActive(item.label);
        navigate(item.link);
      }}
    >
      <item.icon className={classes.linkIcon} stroke={1.5} />
      <span>{item.label}</span>
    </a>
  ));

  const onChange = (event) => {
    const value = event.target.value;
    setSelectedOrgGrp(value);
    // navigate(`/requirements/${value}`);
    window.location.href = window.location.origin + `/requirements/${value}`;
  };

  React.useEffect(() => {
    axiosClientBasic
      .get("/api/org_groups/", {
        headers: {
          authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        },
      })
      .then((response) => {
        setOrgGroups(response.data.results);
      });
  }, []);

  return (
    <>
      <Navbar
        // height={"700vh"}
        width={{ sm: 300 }}
        p="md"
        className={classes.navbar}
        style={{ backgroundColor: "#05447a" }}
      >
        <Navbar.Section grow>
          <Group className={classes.header} position="apart">
            {/* <MantineLogo size={28} inverted /> */}

            <h5 style={{ color: "white" }}>
              <b>REQUIREMENT LIFE CYCLE MANAGER</b>
            </h5>

            <p style={{ color: "white" }}>Org Group</p>

            <Form.Select
              aria-label="Default select example"
              onChange={onChange}
            >
              <option value="default" selected={"default" == orggroup}>
                Default
              </option>
              {orgGroups.map((item) => {
                return (
                  <option value={item.id} selected={item.id == orggroup}>
                    {item.name}
                  </option>
                );
              })}
            </Form.Select>
            {/* <Code className={classes.version}>v1.0</Code> */}
          </Group>
          {links}
        </Navbar.Section>

        <Navbar.Section className={classes.footer}>
          <a
            href="#"
            className={classes.link}
            onClick={(event) => event.preventDefault()}
          >
            <IconUser className={classes.linkIcon} stroke={1.5} />
            <span>{auth.userName.toUpperCase()}</span>
          </a>
          {/* <a
            href="#"
            className={classes.link}
            onClick={(event) => {
              event.preventDefault();
              logout();
            }}
          >
            <IconLogout className={classes.linkIcon} stroke={1.5} />
            <span>Logout</span>
          </a> */}

          <a
            href="#"
            className={classes.link}
            onClick={() => {
              navigate(`/`);
            }}
          >
            <IconTruckReturn className={classes.linkIcon} stroke={1.5} />
            <span>Return to Main Dashboard</span>
          </a>
          <a
            href="#"
            className={classes.link}
            onClick={(event) => event.preventDefault()}
          >
            <IconLogout className={classes.linkIcon} stroke={1.5} />
            <span>Logout</span>
          </a>
        </Navbar.Section>
      </Navbar>
    </>
  );
}
