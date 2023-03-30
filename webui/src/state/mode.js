import { atom } from "recoil";

export const colorScheme = atom({
  key: "colorScheme",
  default: "dark",
});

export const sideBar = atom({
  key: "sideBar",
  default: "open",
});
