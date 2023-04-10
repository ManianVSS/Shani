import React from "react";
import { axiosClient } from "../../api/AxiosInstance";
import { AgGridReact } from "ag-grid-react";
import { useNavigate } from "react-router-dom";

import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";

const Usecases = () => {
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
  const [usecases, setUsecases] = React.useState([]);
  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },
    { headerName: "Name", field: "name" },
    { headerName: "Summary", field: "summary" },
    { headerName: "Usecase Category", field: "category" },
    { headerName: "Consumer Score", field: "consumer_score" },
    { headerName: "Serviceability Score", field: "serviceability_score" },
    { headerName: "Test Confidence", field: "test_confidence" },
    { headerName: "Development Confidence", field: "test_confidence" },
    { headerName: "Weight", field: "weight" },
  ]);
  React.useEffect(() => {
    axiosClient.get("/requirements/api/use_cases/").then((response) => {
      setUsecases(response.data.results);
    });
  }, []);

  return (
    <div className="ag-theme-alpine" style={{ height: "450px" }}>
      <AgGridReact
        rowData={usecases}
        defaultColDef={defaultColDef}
        columnDefs={columnDefs}
        onRowDoubleClicked={(data) => {
          navigate("/usecases/" + data.data.id);
        }}
      ></AgGridReact>
    </div>
  );
};

export default Usecases;
