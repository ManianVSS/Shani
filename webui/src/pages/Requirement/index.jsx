import React from "react";
// import * as React from "react";
import { styled, useTheme } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Drawer from "@mui/material/Drawer";
import MuiAppBar, { AppBarProps as MuiAppBarProps } from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import CssBaseline from "@mui/material/CssBaseline";
import List from "@mui/material/List";
import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import InboxIcon from "@mui/icons-material/MoveToInbox";
import MailIcon from "@mui/icons-material/Mail";
import BreadcrumbComponent from "./BreadcrumbComponent";
import RequirementTable from "./RequirementTable";
import { AgGridReact } from "ag-grid-react";
import { axiosClientBasic } from "../../hooks/api";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";
import { useNavigate, useParams } from "react-router-dom";
import Heading from "../../capacity-planner/components/Heading";
import TreeComponent from "../../components/TreeComponent";
import json from "../../components/TreeComponent/data/json";
import { Col, Row } from "react-bootstrap";
import IndividualReqComponent from "./IndividualReqComponent";

const drawerWidth = 500;

const Main = styled("main", { shouldForwardProp: (prop) => prop !== "open" })(
  ({ theme, open }) => ({
    flexGrow: 1,
    padding: theme.spacing(3),
    transition: theme.transitions.create("margin", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    marginRight: -drawerWidth,
    ...(open && {
      transition: theme.transitions.create("margin", {
        easing: theme.transitions.easing.easeOut,
        duration: theme.transitions.duration.enteringScreen,
      }),
      marginRight: 0,
    }),
    position: "relative",
  })
);

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  transition: theme.transitions.create(["margin", "width"], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(["margin", "width"], {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
    marginRight: drawerWidth,
  }),
}));

const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
  justifyContent: "flex-start",
}));

const Requirement = () => {
  const theme = useTheme();
  const [open, setOpen] = React.useState(true);

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };
  const { orggroup, reqcatid } = useParams();
  const navigate = useNavigate();

  const defaultColDef = {
    sortable: true,
    filter: true,
    resizable: true,
    flex: 1,
    cellStyle: {
      borderColor: "black",
      borderWidth: "1px",
      borderStyle: "solid",
    },
  };
  const [mData, setMData] = React.useState([]);
  const [indiData, setIndiData] = React.useState(null);
  const rowStyle = { textAlign: "center" };
  const getRowStyle = (params) => {
    if (params.data.type == "category") {
      return { background: "#99e6ff" };
    }
  };

  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },

    {
      headerName: "Name",
      field: "name",
    },
    { headerName: "Summary", field: "summary" },
    // { headerName: "Description", field: "description" },
    { headerName: "Org group", field: "org_group" },
  ]);
  let myData = [];
  React.useEffect(() => {
    axiosClientBasic
      .get(
        "/requirements/api/browse_requirements_category?org_group=" +
          (orggroup === "default" ? "" : orggroup) +
          "&requirement_category_id=" +
          (reqcatid === undefined ? "" : reqcatid),
        {
          headers: {
            authorization:
              "Bearer " + window.localStorage.getItem("accessToken"),
          },
        }
      )
      .then((response) => {
        response.data.sub_categories.map((item) =>
          myData.push({
            id: item.id,
            name: item.name,
            summary: item.summary,
            org_group: item.org_group,
            type: "category",
          })
        );
        response.data.requirements.map((item) =>
          myData.push({
            id: item.id,
            name: item.name,
            summary: item.summary,
            org_group: item.org_group,
            type: "requirement",
          })
        );
        setMData(myData);
      });
  }, []);
  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          flexFlow: "row wrap",
        }}
      >
        <div>
          <BreadcrumbComponent />
        </div>
        <div>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="end"
            onClick={handleDrawerOpen}
            sx={{ ...(open && { display: "none" }) }}
          >
            <MenuIcon />
          </IconButton>
        </div>
      </div>
      <Box sx={{ display: "flex" }}>
        <CssBaseline />

        <Main open={open}>
          <div className="ag-theme-alpine" style={{ height: "150px" }}>
            <AgGridReact
              rowStyle={rowStyle}
              // getRowStyle={getRowStyle}
              rowData={mData}
              columnDefs={columnDefs}
              defaultColDef={defaultColDef}
              rowSelection="single"
              onRowDoubleClicked={(data) => {
                if (data.data.type == "category") {
                  window.location =
                    window.location.origin +
                    "/requirements/" +
                    (data.data.org_group === null
                      ? "default"
                      : data.data.org_group) +
                    "/" +
                    data.data.id;
                } else {
                  navigate("/requirement/" + data.data.id);
                }
              }}
              onRowClicked={(data) => {
                setIndiData({ id: data.data.id, type: data.data.type });
              }}
            ></AgGridReact>
          </div>

          {/* <TreeComponent data={json} /> */}
        </Main>
        <Drawer
          sx={{
            width: drawerWidth,
            flexShrink: 0,
            "& .MuiDrawer-paper": {
              width: drawerWidth,
            },
          }}
          variant="persistent"
          anchor="right"
          open={open}
        >
          <DrawerHeader>
            <IconButton onClick={handleDrawerClose}>
              {theme.direction === "rtl" ? (
                <ChevronLeftIcon />
              ) : (
                <ChevronRightIcon />
              )}
            </IconButton>
          </DrawerHeader>
          <Divider />
          <IndividualReqComponent data={indiData} />
        </Drawer>
      </Box>
    </div>
  );
};

export default Requirement;
