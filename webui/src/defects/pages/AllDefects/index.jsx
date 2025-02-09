import { AgGridReact } from "ag-grid-react";
import React from "react";
import { useNavigate } from "react-router-dom";
import { axiosClientBasic } from "../../../hooks/api";

const AllDefects = () => {
  const rowStyle = { textAlign: "center" };
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
    { headerName: "ID", field: "id" },

    {
      headerName: "Release",
      field: "release.name",
    },
    { headerName: "Build", field: "build.name" },

    { headerName: "Summary", field: "summary" },
    { headerName: "Description", field: "description" },
    { headerName: "External ID", field: "external_id" },
    { headerName: "Attachment", field: "details_file" },
    { headerName: "Created on", field: "created_at" },
  ]);
  const [defects, setDefects] = React.useState([]);
  const [indiData, setIndiData] = React.useState(null);
  const navigate = useNavigate();

  React.useEffect(() => {
    axiosClientBasic
      .get("/execution/api/defects/", {
        headers: {
          authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        },
      })
      .then((response) => {
        console.log(response.data);
        setDefects(response.data.results);
      });
  }, []);
  return (
    <div>
      <div className="ag-theme-alpine" style={{ height: "150px" }}>
        <AgGridReact
          rowStyle={rowStyle}
          // getRowStyle={getRowStyle}
          rowData={defects}
          columnDefs={columnDefs}
          defaultColDef={defaultColDef}
          rowSelection="single"
          onRowDoubleClicked={(data) => {
            navigate("/defects/" + data.data.id);
          }}
        ></AgGridReact>
      </div>
    </div>
  );
};

export default AllDefects;
