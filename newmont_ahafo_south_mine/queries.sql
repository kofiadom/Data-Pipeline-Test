-- 1. Which department has the highest average production tonnage?
SELECT Department, AVG(Production_Tonnage) AS Avg_Production_Tonnage
FROM newmont_ahafo_south_mine_dataset
GROUP BY Department
ORDER BY Avg_Production_Tonnage DESC
LIMIT 1;

-- 2. What is the total production cost per equipment type?
SELECT Equipment_Type, SUM(Production_Cost) AS Total_Production_Cost
FROM newmont_ahafo_south_mine_dataset
GROUP BY Equipment_Type;

-- 3. How many safety incidents occurred in each location?
SELECT Location, COUNT(*) AS Safety_Incident_Count
FROM newmont_ahafo_south_mine_dataset
WHERE Safety_Incident = 'Yes'
GROUP BY Location;

-- 4. What is the average maintenance cost for each job title?
SELECT Job_Title, AVG(Maintenance_Cost) AS Avg_Maintenance_Cost
FROM newmont_ahafo_south_mine_dataset
GROUP BY Job_Title;

-- 5. Which shift has the highest average production tonnage?
SELECT Shift, AVG(Production_Tonnage) AS Avg_Production_Tonnage
FROM newmont_ahafo_south_mine_dataset
GROUP BY Shift
ORDER BY Avg_Production_Tonnage DESC
LIMIT 1;

-- 6. How does the average production tonnage vary across different equipment statuses?
SELECT Equipment_Status, AVG(Production_Tonnage) AS Avg_Production_Tonnage
FROM newmont_ahafo_south_mine_dataset
GROUP BY Equipment_Status;

-- 7. What is the total revenue generated from each department?
SELECT Department, SUM(Revenue) AS Total_Revenue
FROM newmont_ahafo_south_mine_dataset
GROUP BY Department;

-- 8. How many environmental incidents occurred in each department?
SELECT Department, COUNT(*) AS Environmental_Incident_Count
FROM newmont_ahafo_south_mine_dataset
WHERE Environmental_Incident = 'Yes'
GROUP BY Department;

-- 9. Which employee has the highest total revenue contribution?
SELECT Employee_Name, SUM(Revenue) AS Total_Revenue_Contribution
FROM newmont_ahafo_south_mine_dataset
GROUP BY Employee_Name
ORDER BY Total_Revenue_Contribution DESC
LIMIT 1;

-- 10. What is the average gold price for each equipment type?
SELECT Equipment_Type, AVG(Gold_Price) AS Avg_Gold_Price
FROM newmont_ahafo_south_mine_dataset
GROUP BY Equipment_Type;
