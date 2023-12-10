import React from "react";
import Styled from "styled-components";
import FolderTree from "./FolderTree";

const StyledContainer = Styled.div`
position: absolute;
top: 50%;
left:50%;
transform: translate(-50%, -50%);
width : 400px;
height: 600px;
overflow-y: auto;
background-color:papayawhip;
padding: 2rem;
border-radius:20px;
`;

const TreeComponent = (props) => {
  return (
    <div>
      <StyledContainer>
        <FolderTree json={props.data} />
      </StyledContainer>
    </div>
  );
};

export default TreeComponent;
