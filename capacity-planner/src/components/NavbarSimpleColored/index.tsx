import { useContext, useState } from "react";
import { createStyles, Navbar, Group, Code } from "@mantine/core";
import {
  IconLogout,
  IconHome,
  IconBook,
  IconUser,
  IconCalendar,
} from "@tabler/icons";
import { useNavigate } from "react-router-dom";
import { authState } from "../../state/authData";
import { useRecoilState } from "recoil";

const useStyles = createStyles((theme, _params, getRef) => {
  const icon = getRef("icon");
  return {
    navbar: {
      backgroundColor: theme.fn.variant({
        variant: "filled",
        color: theme.primaryColor,
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
  { link: "/", label: "HOME", icon: IconHome },
  { link: "/capacity", label: "CAPACITY VIEW", icon: IconBook },
  { link: "/engineer-availability", label: "ENGINEER VIEW", icon: IconUser },
  { link: "/leaves", label: "LEAVES", icon: IconCalendar },
  // { link: "", label: "Databases", icon: IconDatabaseImport },
  // { link: "", label: "Authentication", icon: Icon2fa },
  // { link: "", label: "Other Settings", icon: IconSettings },
];

export function NavbarSimpleColored() {
  const navigate = useNavigate();
  const { classes, cx } = useStyles();
  const [active, setActive] = useState("Billing");
  const [auth, setAuth] = useRecoilState(authState);
  const logout = () => {
    window.localStorage.setItem("accessToken", "");
    window.localStorage.setItem("user", "");
    navigate(`/login`);
    setAuth({
      accessToken: null,
      authStatus: false,
      errorMessage: "",
      userName: "",
    });
  };
  const links = data.map((item) => (
    <a
      className={cx(classes.link, {
        [classes.linkActive]: item.label === active,
      })}
      // href={item.link}
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

  return (
    <>
      <Navbar
        // height={"700vh"}
        width={{ sm: 300 }}
        p="md"
        className={classes.navbar}
      >
        <Navbar.Section grow>
          <Group className={classes.header} position="apart">
            {/* <MantineLogo size={28} inverted /> */}

            <h5 style={{ color: "white" }}>
              <b>CAPACITY PLANNER</b>
            </h5>
            <Code className={classes.version}>v1.0</Code>
          </Group>
          {links}
        </Navbar.Section>

        <Navbar.Section className={classes.footer}>
          {/* <a
            href="#"
            className={classes.link}
            onClick={(event) => event.preventDefault()}
          >
            <IconSwitchHorizontal className={classes.linkIcon} stroke={1.5} />
            <span>Change account</span>
          </a> */}
          {/* <p>{authData.value.user.firstName}</p> */}

          <a
            href="#"
            className={classes.link}
            onClick={(event) => {
              event.preventDefault();
              logout();
            }}
          >
            <IconLogout className={classes.linkIcon} stroke={1.5} />
            <span>Logout</span>
          </a>
        </Navbar.Section>
      </Navbar>
    </>
  );
}
