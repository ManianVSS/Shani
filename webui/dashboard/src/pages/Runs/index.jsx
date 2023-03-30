import React from "react";
import { axiosClient } from "../../api/AxiosInstance";
import { AgGridReact } from "ag-grid-react";

import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";

const Runs = () => {
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
  const [runs, setRuns] = React.useState([]);
  const rowStyle = { textAlign: "center" };
  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },
    { headerName: "Build", field: "build" },
    {
      headerName: "Name",
      field: "name",
    },
  ]);
  React.useEffect(() => {
    axiosClient.get("/runs/").then((response) => {
      setRuns(response.data.results);
    });
  }, []);

  return (
    <div className="ag-theme-alpine" style={{ height: "450px" }}>
      <AgGridReact
        rowStyle={rowStyle}
        rowData={runs}
        columnDefs={columnDefs}
        defaultColDef={defaultColDef}
      ></AgGridReact>
    </div>
  );
};

export default Runs;
