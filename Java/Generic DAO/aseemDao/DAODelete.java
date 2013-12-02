package aseemDao;

import java.sql.Connection;
import java.sql.SQLException;

import aseemEnums.TableName;

public interface DAODelete {

	public abstract <T> boolean deleteFrom(Connection con, TableName tableName,
			T currentPojo) throws SQLException;
}
