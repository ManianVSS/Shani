import React from "react";
import { AgGridReact } from "ag-grid-react";

import { axiosClientForReliability } from "../../reliabilityApi";
import { useNavigate } from "react-router-dom";

const MonitoringDashboard = () => {
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
  const [reliruns, setReliruns] = React.useState([]);
  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },
    {
      headerName: "BUILD",
      field: "build",
    },
    { headerName: "RUN NAME", field: "name" },
    { headerName: "TYPE", field: "type" },
    { headerName: "TEST NAME", field: "testName" },
    { headerName: "STATUS", field: "status" },
  ]);
  React.useEffect(() => {
    axiosClientForReliability
      .get("/execution/api/reliability_runs/")
      .then((response) => {
        setReliruns(response.data.results);
      });
  }, []);

  return (
    <div className="ag-theme-alpine" style={{ height: "450px" }}>
      <AgGridReact
        rowData={reliruns}
        defaultColDef={defaultColDef}
        columnDefs={columnDefs}
        onRowClicked
        onRowDoubleClicked={(data) => {
          navigate("/reliability/monitoring/" + data.data.id);
        }}
      ></AgGridReact>
    </div>
  );
};

export default MonitoringDashboard;
