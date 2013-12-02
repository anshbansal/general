package aseemDao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.naming.NamingException;

import aseemEnums.Databases;

public abstract class DAOFactory {

	// Abstract Instance methods
	public abstract DAOInsert getDAOInsert() throws SQLException;

	public abstract DAORead getDAORead() throws SQLException;

	public abstract DAODelete getDAODelete();

	public abstract DAOUpdate getDAOUpdate();

	// Concrete Class Methods
	public static DAOFactory factoryProducer(Databases db)
			throws NamingException {
		switch (db) {
		case Oracle:
			return new OracleFactory();
		default:
			return null;
		}
	}

	static void closeAll(PreparedStatement ps, ResultSet rs) {
		try {
			rs.close();
		} catch (Exception e) {
		}
		try {
			ps.close();
		} catch (Exception e) {
		}
	}
}
