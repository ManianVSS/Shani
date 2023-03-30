import React from "react";
import "./style.css";
import { useNavigate } from "react-router-dom";

const UsecaseRecord = (props) => {
  const history = useNavigate();
  const handleClick = (e, route) => {
    switch (e.detail) {
      case 1:
        break;
      case 2:
        history(`/usecase/${route}`);
        break;
      case 3:
        break;
      default:
        break;
    }
  };
  return (
    <tbody>
      {props.usecases.map((item) => {
        return (
          <tr onClick={(e) => handleClick(e, item.use_case_id)}>
            <td>{item.use_case_id}</td>
            <td>{item.name}</td>
          </tr>
        );
      })}
    </tbody>
  );
};

export default UsecaseRecord;
