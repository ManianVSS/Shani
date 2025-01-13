import React, { useState } from "react";
import { AgGridReact } from "ag-grid-react";
import { axiosClientForCapacity, axiosClientForLogin } from "../../capacityApi";
import { Container, Form, Row } from "react-bootstrap";
import Heading from "../../components/Heading";
import * as moment from "moment";
// import { useNavigate } from "react-router-dom";

const Holidays = () => {
  // const navigate = useNavigate();
  const [holidays, setHolidays] = React.useState([]);
  const [org, setOrg] = useState("Choose...");
  const [orgData, setOrgData] = useState([]);
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

  const [columnDefs] = React.useState([
    // { headerName: "ID", field: "id" },
    { headerName: "NAME", field: "name" },
    {
      headerName: "DATE",
      field: "date",
      cellRenderer: (data) => {
        return data.value ? moment(data.value).format("D MMM YYYY") : "";
      },
    },
    // { headerName: "SITE", field: "site" },
  ]);
  React.useEffect(() => {
    axiosClientForLogin
      .get("/sites/", {
        // headers: {
        //   authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        // },
      })
      .then((response) => {
        setOrgData(response.data.results);
        setOrg(response.data.results[0]);
        getHolidayData(response.data.results[0].id);
      });
  }, []);

  const getHolidayData = (siteID) => {
    axiosClientForCapacity
      .get("/people/api/site_holidays/?site=" + siteID, {
        // headers: {
        //   authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        // },
      })
      .then((response) => {
        setHolidays(response.data.results);
      });
  };

  return (
    <div>
      <Heading heading={"HOLIDAYS LIST"} />
      <Container>
        <Form>
          <Row className="mb-3">
            <Form.Group as={Row} controlId="formGridState">
              <Form.Label>LOCATION</Form.Label>
              <Form.Select
                // defaultValue="Choose..."
                onChange={(event) => {
                  axiosClientForLogin
                    .get("/sites/" + event.target.value, {
                      headers: {
                        authorization:
                          "Bearer " +
                          window.localStorage.getItem("accessToken"),
                      },
                    })
                    .then((response) => {
                      setOrg(response.data);
                    });

                  getHolidayData(event.target.value);
                }}
              >
                {/* <option>Choose...</option> */}
                {orgData.map((item) => {
                  return (
                    <option value={item.id} key={item.id}>
                      {item.name}
                    </option>
                  );
                })}
              </Form.Select>
            </Form.Group>
          </Row>
        </Form>
      </Container>
      <div className="ag-theme-alpine" style={{ height: "450px" }}>
        <AgGridReact
          rowData={holidays}
          defaultColDef={defaultColDef}
          columnDefs={columnDefs}
          onRowClicked
        ></AgGridReact>
      </div>
    </div>
  );
};

export default Holidays;
