import React from "react";
import { axiosClient } from "../../api/AxiosInstance";
import { AgGridReact } from "ag-grid-react";
import { useNavigate } from "react-router-dom";

import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";

const Features = () => {
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
  const [features, setFeatures] = React.useState([]);
  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },
    { headerName: "Name", field: "name" },
    { headerName: "Summary", field: "summary" },
    { headerName: "Weight", field: "weight" },
  ]);
  React.useEffect(() => {
    axiosClient.get("/features/").then((response) => {
      setFeatures(response.data.results);
    });
  }, []);

  return (
    <div className="ag-theme-alpine" style={{ height: "450px" }}>
      <AgGridReact
        rowData={features}
        defaultColDef={defaultColDef}
        columnDefs={columnDefs}
        onRowDoubleClicked={(data) => {
          navigate("/features/" + data.data.id);
        }}
      ></AgGridReact>
    </div>
  );
};

export default Features;
