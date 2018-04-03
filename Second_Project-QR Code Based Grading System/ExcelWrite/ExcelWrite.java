/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package excelwrite;
 
import java.io.FileOutputStream;
import java.io.IOException;
 
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
 
/**
 * A very simple program that writes some data to an Excel file
 * using the Apache POI library.
 * @author www.codejava.net
 *
 */
public class ExcelWrite {
 
    public static void main(String[] args) throws IOException {
        XSSFWorkbook workbook = new XSSFWorkbook();
        XSSFSheet sheet = workbook.createSheet("Öğrenci notları");
         
        Object[][] bookData = {
                {"Öğrenci isimleri","ID","Notlar"},
                {"Furkan Vardar", "123", 79},
                {"Muhammed Kostekli", "234523", 36.5},
                {"Ilkay Devran", "52312", 42},
                {"Şafak Topçu", "1234567", 99},
        };
 
        int rowCount = 0;
        for (Object[] aBook : bookData) {
            Row row = sheet.createRow(++rowCount);
             
            int columnCount = 0;
             
            for (Object field : aBook) {
                Cell cell = row.createCell(++columnCount);
                if (field instanceof String) {
                    cell.setCellValue((String) field);
                } else if (field instanceof Integer) {
                    cell.setCellValue((Integer) field);
                } else if (field instanceof Double){
                    cell.setCellValue((Double) field);
                }
            }
             
        }
         
        try (FileOutputStream outputStream = new FileOutputStream("JavaBooks.xlsx")) {
            workbook.write(outputStream);
        }
    }
 
}