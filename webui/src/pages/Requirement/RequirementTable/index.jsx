import React from "react";
import ReactDOM from "react-dom";
import "./style.css";
// import "rsuite/dist/rsuite.css";
import { useWindowSize } from "../../../hooks/windowSize";

import {
  Table,
  Popover,
  Whisper,
  Checkbox,
  Dropdown,
  IconButton,
  Progress,
  Pagination,
} from "rsuite";
import MoreIcon from "@rsuite/icons/legacy/More";
import { mockUsers } from "../../../data/mockData/mock";

const { Column, HeaderCell, Cell } = Table;
const defaultData = mockUsers(100);

const NameCell = ({ rowData, dataKey, onClick, ...props }) => {
  const speaker = (
    <Popover title="Description">
      <p>
        <b>Name:</b> {rowData.name}
      </p>
      <p>
        <b>Gender:</b> {rowData.gender}
      </p>
      <p>
        <b>City:</b> {rowData.city}
      </p>
      <p>
        <b>Street:</b> {rowData.street}
      </p>
    </Popover>
  );

  return (
    <Cell {...props} value={rowData[dataKey]} onClick={onClick}>
      <Whisper placement="top" speaker={speaker}>
        <a>{rowData[dataKey]}</a>
      </Whisper>
    </Cell>
  );
};

const ImageCell = ({ rowData, dataKey, ...props }) => (
  <Cell {...props} style={{ padding: 0 }}>
    <div
      style={{
        width: 40,
        height: 40,
        background: "#f5f5f5",
        borderRadius: 6,
        marginTop: 2,
        overflow: "hidden",
        display: "inline-block",
      }}
    >
      <img src={rowData.avatar} width="40" />
    </div>
  </Cell>
);

const CheckCell = ({ rowData, onChange, checkedKeys, dataKey, ...props }) => (
  <Cell {...props} style={{ padding: 0 }}>
    <div style={{ lineHeight: "46px" }}>
      <Checkbox
        value={rowData[dataKey]}
        inline
        onChange={onChange}
        checked={checkedKeys.some((item) => item === rowData[dataKey])}
      />
    </div>
  </Cell>
);

const renderMenu = ({ onClose, left, top, className }, ref) => {
  const handleSelect = (eventKey) => {
    onClose();
    console.log(eventKey);
  };
  return (
    <Popover ref={ref} className={className} style={{ left, top }} full>
      <Dropdown.Menu onSelect={handleSelect}>
        <Dropdown.Item eventKey={1}>Follow</Dropdown.Item>
        <Dropdown.Item eventKey={2}>Sponsor</Dropdown.Item>
        <Dropdown.Item eventKey={3}>Add to friends</Dropdown.Item>
        <Dropdown.Item eventKey={4}>View Profile</Dropdown.Item>
        <Dropdown.Item eventKey={5}>Block</Dropdown.Item>
      </Dropdown.Menu>
    </Popover>
  );
};

const ActionCell = ({ rowData, dataKey, ...props }) => {
  return (
    <Cell {...props} className="link-group">
      <Whisper
        placement="autoVerticalStart"
        trigger="click"
        speaker={renderMenu}
      >
        <IconButton appearance="subtle" icon={<MoreIcon />} />
      </Whisper>
    </Cell>
  );
};

const RequirementTable = () => {
  const [limit, setLimit] = React.useState(10);
  const [page, setPage] = React.useState(1);

  const handleChangeLimit = (dataKey) => {
    setPage(1);
    setLimit(dataKey);
  };

  const data = defaultData.filter((v, i) => {
    const start = limit * (page - 1);
    const end = start + limit;
    return i >= start && i < end;
  });

  const pageSize = useWindowSize();
  const [checkedKeys, setCheckedKeys] = React.useState([]);
  let checked = false;
  let indeterminate = false;

  if (checkedKeys.length === data.length) {
    checked = true;
  } else if (checkedKeys.length === 0) {
    checked = false;
  } else if (checkedKeys.length > 0 && checkedKeys.length < data.length) {
    indeterminate = true;
  }

  const handleCheckAll = (value, checked) => {
    const keys = checked ? data.map((item) => item.id) : [];
    setCheckedKeys(keys);
  };
  const handleCheck = (value, checked) => {
    console.log(value);
    const keys = checked
      ? [...checkedKeys, value]
      : checkedKeys.filter((item) => item !== value);
    setCheckedKeys(keys);
  };
  // console.log(data[checkedKeys]);
  // console.log(checkedKeys);
  const onclickName = (value) => {
    console.log(value);
  };
  return (
    <div>
      <Table height={pageSize.height * 0.78} data={data} id="table">
        <Column width={0.059523 * pageSize.width} align="center">
          <HeaderCell style={{ padding: 0 }}>
            <div style={{ lineHeight: "40px" }}>
              <Checkbox
                inline
                checked={checked}
                indeterminate={indeterminate}
                onChange={handleCheckAll}
              />
            </div>
          </HeaderCell>
          <CheckCell
            dataKey="id"
            checkedKeys={checkedKeys}
            onChange={handleCheck}
          />
        </Column>
        <Column width={0.095238 * pageSize.width} align="center">
          <HeaderCell>Avartar</HeaderCell>
          <ImageCell dataKey="avartar" />
        </Column>

        <Column width={0.0714285 * pageSize.width}>
          <HeaderCell>Name</HeaderCell>
          <NameCell dataKey="name" onClick={(event) => onclickName(event)} />
        </Column>

        <Column width={0.2738095 * pageSize.width}>
          <HeaderCell>Skill Proficiency</HeaderCell>
          <Cell style={{ padding: "10px 0" }}>
            {(rowData) => (
              <Progress percent={rowData.progress} showInfo={false} />
            )}
          </Cell>
        </Column>

        <Column width={0.1190476 * pageSize.width}>
          <HeaderCell>Rating</HeaderCell>
          <Cell>
            {(rowData) =>
              Array.from({ length: rowData.rating }).map((_, i) => (
                <span key={i}>⭐️</span>
              ))
            }
          </Cell>
        </Column>

        <Column width={0.1190476 * pageSize.width}>
          <HeaderCell>Income</HeaderCell>
          <Cell>{(rowData) => `$${rowData.amount}`}</Cell>
        </Column>

        <Column width={0.09 * pageSize.width}>
          <HeaderCell>
            <MoreIcon />
          </HeaderCell>
          <ActionCell dataKey="id" />
        </Column>
      </Table>
      <div style={{ padding: 20 }}>
        <Pagination
          prev
          next
          first
          last
          ellipsis
          boundaryLinks
          maxButtons={5}
          size="xs"
          layout={["total", "-", "limit", "|", "pager", "skip"]}
          total={defaultData.length}
          limitOptions={[10, 30, 50]}
          limit={limit}
          activePage={page}
          onChangePage={setPage}
          onChangeLimit={handleChangeLimit}
        />
      </div>
    </div>
  );
};

export default RequirementTable;
