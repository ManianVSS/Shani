import React from "react";
import { axiosClient } from "../../api/AxiosInstance";
import { AgGridReact } from "ag-grid-react";
import { useNavigate } from "react-router-dom";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";

const Testcases = () => {
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
  const [testcases, setTestcases] = React.useState([]);
  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },
    { headerName: "Name", field: "name" },
    { headerName: "Summary", field: "summary" },
    { headerName: "Status", field: "status" },
    { headerName: "Automated", field: "automated" },
  ]);
  React.useEffect(() => {
    axiosClient.get("/testdesign/api/testcases/").then((response) => {
      setTestcases(response.data.results);
    });
  }, []);

  return (
    <div className="ag-theme-alpine" style={{ height: "450px" }}>
      <AgGridReact
        rowData={testcases}
        defaultColDef={defaultColDef}
        columnDefs={columnDefs}
        onRowDoubleClicked={(data) => {
          navigate("/testcases/" + data.data.id);
        }}
      ></AgGridReact>
    </div>
  );
};

export default Testcases;
