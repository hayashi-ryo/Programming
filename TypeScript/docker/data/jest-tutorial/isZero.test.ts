import { isZero } from "./isZero";

test("true case", () => {
  const result = isZero(0);
  expect(result).toBe(true);
})

test("false case 1", () => {
  const result = isZero(1);
  expect(result).toBe(false);
})

test("false case 2", () => {
  const result = isZero(999999999999999999);
  expect(result).toBe(false);
})