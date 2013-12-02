package aseemDao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import aseemEnums.TableName;
import aseemPojo.Student;

public class SpecStudent {
	public static Student getPojo(ResultSet rs) throws SQLException {
		Student currentStudent = new Student();
		currentStudent.setStudentId(rs.getString("Student_Id"));
		currentStudent.setRollNo(rs.getString("Roll_No"));
		currentStudent.setStudentName(rs.getString("Student_Name"));
		currentStudent.setAddress(rs.getString("Address"));
		currentStudent.setEmail(rs.getString("Email"));
		currentStudent.setContactNumber(rs.getString("Contact_Number"));
		currentStudent.setGuardianName(rs.getString("Guardian_Name"));
		currentStudent.setEnrollmentDate(rs.getDate("Enrollment_Date"));
		return currentStudent;
	}

	public static <T> PreparedStatement getPreparedInsert(Connection con,
			TableName tableName, T currentPojo) throws SQLException {
		Student currentStudent = (Student) currentPojo;
		PreparedStatement ps = con.prepareStatement("Insert into " + tableName
				+ " VALUES(?, ?, ?, ?, ?, ?, ?, ?)");
		ps.setString(1, currentStudent.getStudentId());
		ps.setString(2, currentStudent.getRollNo());
		ps.setString(3, currentStudent.getStudentName());
		ps.setString(4, currentStudent.getAddress());
		ps.setString(5, currentStudent.getEmail());
		ps.setString(6, currentStudent.getContactNumber());
		ps.setString(7, currentStudent.getGuardianName());
		ps.setDate(8, currentStudent.getEnrollmentDate());
		return ps;
	}

	public static <T> PreparedStatement getPreparedInsertRunning(
			Connection con, TableName tableName, T currentPojo)
			throws SQLException {
		Student currentStudent = (Student) currentPojo;
		PreparedStatement ps = con.prepareStatement("Insert into " + tableName
				+ " VALUES(aseem_sequence.nextval, ?, ?, ?, ?, ?, ?, ?)");
		ps.setString(1, currentStudent.getRollNo());
		ps.setString(2, currentStudent.getStudentName());
		ps.setString(3, currentStudent.getAddress());
		ps.setString(4, currentStudent.getEmail());
		ps.setString(5, currentStudent.getContactNumber());
		ps.setString(6, currentStudent.getGuardianName());
		ps.setDate(7, currentStudent.getEnrollmentDate());
		return ps;
	}

	public static <T> PreparedStatement getPreparedUpdate(Connection con,
			TableName tableName, T oldPojo, T currentPojo) throws SQLException {
		Student currentStudent = (Student) currentPojo;
		Student oldStudent = (Student) oldPojo;
		PreparedStatement ps = con.prepareStatement("UPDATE " + tableName
				+ " SET Roll_No = ?, Student_Name = ?, Address = ?, "
				+ "Email = ?, ContactNumber = ?, Guardian_Name = ?, "
				+ "Enrollment_Date = ? WHERE Student_Id = ?");
		ps.setString(1, currentStudent.getRollNo());
		ps.setString(2, currentStudent.getStudentName());
		ps.setString(3, currentStudent.getAddress());
		ps.setString(4, currentStudent.getEmail());
		ps.setString(5, currentStudent.getContactNumber());
		ps.setString(6, currentStudent.getGuardianName());
		ps.setDate(7, currentStudent.getEnrollmentDate());
		ps.setString(8, oldStudent.getStudentId());

		return ps;
	}
}
